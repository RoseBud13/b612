<template>
    <div class="login" v-if="state.showLogin">
        <div class="back-drop" @click="toggleLoginModal(state.showLogin)"></div>
        <div class="login-card">
            <space-embed></space-embed>
            <div class="container">
                <div class="register-box" :class="state.registerBoxClass">
                    <h2 class="register-title" @click="showRegisterCard()">
                        <span>没有账号，去</span>注册
                    </h2>
                    <div class="bp-box" :class="state.bpBoxClass">
                        <div class="promote-text">
                            欢迎注册B612
                        </div>
                        <div class="input-box">
                            <input type="text" :placeholder="state.bpCheckInputText" v-model="state.bpCode" @keyup.enter="initBpVerify()">
                        </div>
                        <button id="bp-check" @click="initBpVerify()">{{ state.bpCheckBtnText }}</button>
                    </div>
                    <div class="signup-box" :class="state.signUpBoxClass">
                        <div class="promote-text">
                            请填写账号信息
                        </div>
                        <div class="input-box">
                            <input type="text" placeholder="用户名">
                            <input type="password" placeholder="密码">
                            <input type="password" placeholder="确认密码">
                        </div>
                        <div class="bp-back" @click="backToBpCard()">返回</div>
                        <button>注册</button>
                    </div>
                </div>
                <div class="login-box" :class="state.loginBoxClass">
                    <div class="little-prince">
                        <img src="../assets/img/prince.png" alt="little-prince">
                    </div>
                    <div class="center">
                        <h2 class="login-title" @click="showLoginCard()">
                            <span>已有账号，去</span>登录
                        </h2>
                        <div class="input-box">
                            <input type="text" placeholder="用户名">
                            <input type="password" placeholder="密码">
                        </div>
                        <button>登录</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { defineComponent, reactive, watch, getCurrentInstance } from 'vue';
import { useStore } from 'vuex';
import { verifyBpCode } from "../api";
import { mapMutations } from '../utils/map-state';
import SpaceEmbed from './SpaceEmbed.vue';

export default defineComponent({
    components: {
        SpaceEmbed
    },
    setup() {
        const store = useStore();

        const { proxy } = getCurrentInstance();

        const state = reactive({
            signUpBoxClass: '',
            bpBoxClass: '',
            registerBoxClass: '',
            loginBoxClass: 'slide-up',
            showLogin: store.state.showLogin,
            bpCheckInputText: '邀请码',
            bpCheckBtnText: '验证',
            bpCode: ''
        });

        watch(
            () => store.state.showLogin,
            (showLogin) => {
                state.showLogin = showLogin;
            }
        );

        const { toggleLoginModal } = mapMutations();

        const initBpVerify = () => {
            state.bpCheckBtnText = '验证中...';
            if (state.bpCode != '') {
                let data = {'passcode': state.bpCode};
                verifyBpCode(data).then(res => {
                    console.log(res.data);
                    if (res.data.status) {
                        state.signUpBoxClass = 'bp-toggle-on';
                        state.bpBoxClass = 'bp-toggle-off';
                        state.bpCode = '';
                        state.bpCheckInputText = '邀请码';
                        state.bpCheckBtnText = '验证';
                        proxy.$toast('验证成功', 'success', 2000);
                    } else {
                        state.bpCode = '';
                        state.bpCheckInputText = '请重新填写邀请码';
                        state.bpCheckBtnText = '验证';
                        proxy.$toast('邀请码验证失败', 'error', 2000);
                    }
                }).catch(e => {
                    console.log(e);
                })
            } else {
                state.bpCheckInputText = '请填写邀请码';
                state.bpCheckBtnText = '验证';
                proxy.$toast('邀请码不能为空', 'warning', 2000);
            }
        };

        const backToBpCard = () => {
            state.signUpBoxClass = '';
            state.bpBoxClass = '';
        };

        const showLoginCard = () => {
            if (state.loginBoxClass == 'slide-up') {
                state.registerBoxClass = 'slide-up';
                state.loginBoxClass = '';
            }
        };

        const showRegisterCard = () => {
            if (state.registerBoxClass == 'slide-up') {
                state.loginBoxClass = 'slide-up';
                state.registerBoxClass = '';
            }
        };

        return {
            state,
            toggleLoginModal,
            initBpVerify,
            backToBpCard,
            showLoginCard,
            showRegisterCard
        }
    }
    // data() {
    //     return {
    //         signUpBoxClass: '',
    //         bpBoxClass: '',
    //         registerBoxClass: '',
    //         loginBoxClass: 'slide-up',
    //         showLogin: this.$store.state.showLogin,
    //         bpCheckInputText: '邀请码',
    //         bpCheckBtnText: '验证',
    //         bpCode: ''
    //     }
    // },
    // methods: {
    //      ...mapMutations(['toggleLoginModal']),

    //     initBpVerify() {
    //         this.bpCheckBtnText = '验证中...';
    //         if (this.bpCode != '') {
    //             let data = {'passcode': this.bpCode};

    //             verifyBpCode(data).then(res => {
    //                 console.log(res.data);
    //                 if (res.data.status) {
    //                     this.signUpBoxClass = 'bp-toggle-on';
    //                     this.bpBoxClass = 'bp-toggle-off';
    //                     this.bpCheckBtnText = '验证';
    //                 } else {
    //                     this.bpCheckBtnText = '验证失败';
    //                 }
    //             }).catch(e => {
    //                 console.log(e);
    //             })
    //         } else {
    //             this.bpCheckInputText = '请填写邀请码';
    //             this.bpCheckBtnText = '验证';
    //         }
    //     },
    //     backToBpCard() {
    //         this.signUpBoxClass = '';
    //         this.bpBoxClass = '';
    //     },
    //     showLoginCard() {
    //         if (this.loginBoxClass == 'slide-up') {
    //             this.registerBoxClass = 'slide-up';
    //             this.loginBoxClass = '';
    //         }
    //     },
    //     showRegisterCard() {
    //         if (this.registerBoxClass == 'slide-up') {
    //             this.loginBoxClass = 'slide-up';
    //             this.registerBoxClass = '';
    //         }
    //     }
    // },
    // watch: {
    //     '$store.state.showLogin'(newVal, oldVal) {
    //         this.showLogin = newVal
    //     }
    // }
})
</script>

<style lang="scss" scoped>
.login {
    height: 100vh;
    width: 100vw;
    z-index: 200;
    // display: none;
    // visibility: hidden;
    // opacity: 0;
    // pointer-events: none;
    // transition: all 0.5s;
}
.back-drop {
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    background-color: rgba(0, 0, 0, 0.3);
    z-index: 201;
}
.login-card {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 350px;
    height: 550px;
    border-radius: 15px;
    z-index: 201;
}
.container {
    border-radius: 15px;
    width: 350px;
    height: 550px;
    overflow: hidden;
    position: relative;
}

/* 注册区域（登录区域很多样式和注册区域的一样，故而一些统一的样式写在了一起） */
.register-box {
    width: 70%;
    height: 80%;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%,-50%);
    z-index: 1;
    transition: 0.3s ease;
}
.bp-box,
.signup-box {
    margin: 0;
    padding: 0;
    position: absolute;
    top: 50%;
    left: 0;
    transform: translateY(-50%);
    width: 100%;
    transition: 0.3s ease;
}
.bp-box {
    left: 0;
}
.signup-box {
    left: 130%;
}
.bp-toggle-on {
    left: 0;
}
.bp-toggle-off {
    left: -130%;
}
.register-title,
.login-title {
    color: #fff;
    font-size: 27px;
    text-align: center;
}
.register-title span {
    color: rgba(255,255,255,0.4);
    display: none;
}
.login-title span {
    color: rgba(0,0,0,0.4);
    display: none;
}
.promote-text {
    color: #fff;
    font-size: 20px;
    text-align: center;
}
.register-box .input-box,
.login-box .input-box {
    background-color: #fff;
    border-radius: 15px;
    overflow: hidden;
    margin-top: 20px;
    opacity: 1;
    visibility: visible;
    transition: 0.6s ease;
}
.register-box input,
.login-box input {
    width: 100%;
    height: 30px;
    border: none;
    border-bottom: 1px solid rgba(0,0,0,0.1);
    font-size: 16px;
    padding: 8px 0;
    text-indent: 15px;
    outline: none;
}
.register-box input:last-child,
.login-box input:last-child {
    border-bottom: none;
}
.register-box input::placeholder,
.login-box input::placeholder {
    color: rgba(0,0,0,0.4);
}

.register-box button,
.login-box button {
    width: 100%;
    padding: 13px 45px;
    margin: 15px 0;
    background: rgba(255,255,255,0.4);
    border: none;
    border-radius: 15px;
    color: rgba(0,0,0,0.8);
    font-size: 15px;
    font-weight: bold;
    cursor: pointer;
    opacity: 1;
    visibility: visible;
    transition: 0.3s ease;
}
.register-box button:hover,
.login-box button:hover {
    background-color: rgb(95, 140, 128);
    color: rgba(255,255,255,0.8);
}
.bp-back {
    text-align: center;
    cursor: pointer;
    margin-top: 10px;
    color: rgba(255,255,255,0.8);
}

/* 登录区域 */
.login-box{
    position: absolute;
    inset: 0;
    top: 20%;
    z-index: 2;
    background-color: #fff;
    transition: 0.3s ease;
}
.login-box::before{
    content: "";
    background-color: #fff;
    width: 200%;
    height: 250px;
    border-radius: 50%;
    position: absolute;
    top: -20px;
    left: 50%;
    transform: translateX(-50%);
}
.login-box .little-prince {
    position: relative;
    width: 100%;
    height: 50px;
}
.login-box .little-prince img {
    position: absolute;
    right: 0;
    top: -180%;
    height: 100px;
    width: 100px;
}
.login-box .center{
    width: 70%;
    position: absolute;
    z-index: 3;
    left: 50%;
    top: 40%;
    transform: translate(-50%,-50%);
}
.login-title{
    color: #000;
}
.login-box .input-box{
    border: 1px solid rgba(0,0,0,0.1);
}
.login-box button{
    background-color: #75a297;
}

/* 注册、登录区域收起 */
.login-box.slide-up{
    top: 90%;
}
.login-box.slide-up .center{
    top: 10%;
    transform: translate(-50%,0%);
}
.login-box.slide-up .login-title,
.register-box.slide-up .register-title{
    font-size: 16px;
    cursor: pointer;
}
.login-box.slide-up .login-title span,
.register-box.slide-up .register-title span{
    margin-right: 5px;
    display: inline-block;
}
.login-box.slide-up .input-box,
.login-box.slide-up .button,
.register-box.slide-up .input-box,
.register-box.slide-up .button{
    opacity: 0;
    visibility: hidden;
}
.register-box.slide-up{
    top: 6%;
    transform: translate(-50%,0%);
}

// .show {
//     // display: block;
//     visibility: visible;
//     opacity: 1;
//     pointer-events: auto;
// }
</style>
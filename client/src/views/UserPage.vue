<template>
    <div>
        <space></space>
        <nav-bar></nav-bar>
        <div class="login-card">
            <div class="info-area">
                <div class="avatar-box">
                    <img class="avatar" :src="state.userAvatarUrl"/>
                </div>
                <div class="data-box">

                </div>
            </div>
            <div class="table-area">
                <div class="table-row">
                    <div class="row-name">
                        📮邮箱
                        <span v-if="!state.isEditableEmail" @click="toggleEdit('email')">点击修改</span>
                        <span v-else @click="toggleEdit('email')">点击取消修改</span>
                    </div>
                    <div class="row-data">
                        <p v-if="!state.isEditableEmail">{{ state.userEmail }}</p>
                        <input v-else type="text" :placeholder="state.emailInputText" v-model="state.newEmail">
                    </div>
                </div>
                <div class="table-row">
                    <div class="row-name">
                        🏷昵称
                        <span v-if="!state.isEditableName" @click="toggleEdit('name')">点击修改</span>
                        <span v-else @click="toggleEdit('name')">点击取消修改</span>
                    </div>
                    <div class="row-data">
                        <p v-if="!state.isEditableName">{{ state.userName }}</p>
                        <input v-else type="text" :placeholder="state.nameInputText" v-model="state.newName">
                    </div>
                </div>
                <div class="table-row">
                    <div class="row-name">
                        🎁心情
                        <span v-if="!state.isEditableProfile" @click="toggleEdit('profile')">点击修改</span>
                        <span v-else @click="toggleEdit('profile')">点击取消修改</span>
                    </div>
                    <div class="row-data">
                        <p v-if="!state.isEditableProfile">{{ state.userProfile }}</p>
                        <textarea v-else :placeholder="state.profileInputText" v-model="state.newProfile" rows="3" maxlength="200"></textarea>
                    </div>
                </div>
                <div class="save-data-btn" v-if="state.isEditableEmail || state.isEditableName || state.isEditableProfile">
                    <button @click="updateUserData">{{ state.editBtnText }}</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { defineComponent, reactive, watch, getCurrentInstance, onMounted } from 'vue';
import { useStore } from 'vuex';
import { getUser, updateUser } from "../api";
import { mapMutations } from '../utils/map-state';
import Space from '../components/Space.vue'
import NavBar from "../components/NavBar.vue"

export default defineComponent({
    components: {
        Space,
        NavBar
    },
    setup() {
        const store = useStore();

        const { proxy } = getCurrentInstance();

        const { updateUserInfo } = mapMutations();

        onMounted(() => {
            getUserData();
        });

        // watch(
        //     () => store.state.userInfo,
        //     (userInfo) => {
        //         state.userEmail = userInfo.email;
        //         state.userName = userInfo.name;
        //         state.userAvatarUrl = userInfo.avatar;
        //         state.userProfile = userInfo.profile;
        //     }
        // );

        const state = reactive({
            userEmail: '',
            userName: '',
            userAvatarUrl: '',
            userProfile: '',
            isEditableEmail: false,
            isEditableName: false,
            isEditableProfile: false,
            emailInputText: '请输入新的邮箱',
            nameInputText: '请输入新的昵称',
            profileInputText: '最近过得怎么样？',
            editBtnText: '保存',
            newEmail:  '',
            newName:  '',
            newProfile: ''
            // userEmail: store.state.userInfo.email && store.state.userInfo.email.startsWith('unset_')? '暂无邮箱': store.state.userInfo.email,
            // userName: store.state.userInfo.username && store.state.userInfo.name.startsWith('unset_')? '暂无昵称': store.state.userInfo.name,
            // userAvatarUrl: store.state.userInfo.avatar? store.state.userInfo.avatar : 'https://b612-static-rsrcs-1306125602.cos.ap-shanghai.myqcloud.com/user-avatar%2Fdefault-avatar.png',
            // userProfile: '',
            // isEditable: false,
            // emailInputText: '',
            // nameInputText: '',
            // profileInputText: '',
            // editBtnText: '保存',
            // newEmail:  store.state.userInfo.email && store.state.userInfo.email.startsWith('unset_')? '暂无邮箱': store.state.userInfo.email,
            // newName:  store.state.userInfo.name && store.state.userInfo.name.startsWith('unset_')? '暂无邮箱': store.state.userInfo.name,
            // newProfile: ''
        });

        const getUserData = () => {
            const uid = store.state.userInfo.uid;
            console.log(uid);
            if (uid) {
                getUser(uid).then(res => {
                    console.log(res.data);
                    if (res.data.status) {
                        state.userEmail = res.data.user.email.startsWith('unset_')? '暂无邮箱': res.data.user.email;
                        state.userName = res.data.user.name.startsWith('unset_')? '暂无昵称': res.data.user.name;
                        state.userAvatarUrl = res.data.user.avatar_url? res.data.user.avatar_url: 'https://b612-static-rsrcs-1306125602.cos.ap-shanghai.myqcloud.com/user-avatar%2Fdefault-avatar.png';
                        state.userProfile = res.data.user.profile;
                        // const newUserInfo = {
                        //     'uid': res.data.user.uid,
                        //     'username': res.data.user.username,
                        //     'name': res.data.user.name,
                        //     'email': res.data.user.email,
                        //     'avatar': res.data.user.avatar_url
                        // };
                        // updateUserInfo(newUserInfo);
                    }
                }).catch(e => {
                    console.log(e);
                })
            }
        }

        const updateUserData = () => {
            state.editBtnText = '保存中...';

            const reg = /^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;

            if (state.isEditableEmail && !reg.test(state.newEmail)) {
                state.emailInputText= '请输入有效邮箱';
                state.editBtnText = '保存';
                proxy.$toast('邮箱格式不正确', 'warning', 2000);
                return false;
            };
            if (state.isEditableName && state.newName == '') {
                state.nameInputText = '请输入昵称';
                state.editBtnText = '保存';
                proxy.$toast('昵称不能为空', 'warning', 2000);
                return false;
            };

            let newData = {};

            if (state.isEditableEmail) {
                newData['email'] = state.newEmail;
            };
            if (state.isEditableName) {
                newData['name'] = state.newName;
            };
            if (state.isEditableProfile) {
                newData['profile'] = state.newProfile;
            };

            const current_uid = store.state.userInfo.uid;

            console.log(newData);

            updateUser(current_uid, newData).then(res => {
                console.log(res.data);
                if (res.data.status) {
                    state.userEmail = res.data.user.email;
                    state.userName = res.data.user.name;
                    state.userProfile = res.data.user.profile;
                    const newUserInfo = res.data.user;
                    updateUserInfo(newUserInfo);
                    state.editBtnText = '保存';
                    proxy.$toast('信息修改成功', 'success', 2000);
                    toggleEdit('all');
                } else {
                    switch(res.data.code) {
                        case 401:
                            state.newEmail = '';
                            state.newName = '';
                            state.newProfile = '';
                            state.emailInputText= '';
                            state.nameInputText = '';
                            state.editBtnText = '保存'
                            proxy.$toast('无权限修改', 'error', 2000);
                            break;
                        case 409:
                            state.newEmail = '';
                            state.emailInputText= '请重新输入邮箱';
                            state.editBtnText = '保存'
                            proxy.$toast('邮箱已被使用', 'error', 2000);
                    }
                }
            })
        }

        const toggleEdit = (item) => {
            switch(item) {
                case 'all':
                    state.isEditableEmail = false;
                    state.isEditableName = false;
                    state.isEditableProfile = false;
                    break;
                case 'email':
                    state.isEditableEmail = !state.isEditableEmail;
                    break;
                case 'name':
                    state.isEditableName = !state.isEditableName;
                    break;
                case 'profile':
                    state.isEditableProfile = !state.isEditableProfile;
            }
        }

        return {
            state,
            toggleEdit,
            updateUserData
        }
    }
})
</script>

<style lang="scss" scoped>
.login-card {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 750px;
    height: 550px;
    border-radius: 15px;
    background-color: rgba(255, 255, 255, 0.7);

    display: flex;
    // * {
    //     border: red solid 1px;
    // }
}

.info-area {
    flex: 1;
    height: 100%;
    display: flex;
    flex-direction: column;
}

.avatar-box {
    width: 100%;
    flex: 2;
    display: flex;
    align-items: center;
    justify-content: center;
}

.avatar {
    width: 50%;
    aspect-ratio: auto 1 / 1; 
    border-radius: 50%;
}

.data-box {
    width: 100%;
    flex: 3;
}

.table-area {
    flex: 2;
    height: 100%;
    display: flex;
    flex-direction: column;
}

.table-row {
    width: 100%;
    min-height: 50px;
    padding: 30px 0 20px 0;
}

.row-name {
    width: 70%;
    padding: 5px;
    font-size: 0.9rem;
    color: rgb(80, 80, 80);
    border-bottom: rgb(173, 173, 173) solid 1px;
    position: relative;
}

.row-name span {
    font-size: 0.8rem;
    color: rgba(80, 80, 80, 0.8);
    cursor: pointer;
    position: absolute;
    right: 0;
}

.row-data {
    margin-top: 10px;
}

.row-data p {
    height: 38px;
}

.row-data input {
    width: 70%;
    height: 20px;
    background-color: #eee;
    border: 1px solid rgba(0,0,0,0.1);
    border-radius: 10px;
    font-size: 16px;
    padding: 8px 0;
    text-indent: 15px;
    outline: none;
}

.row-data textarea {
    width: 70%;
    height: 50px;
    background-color: #eee;
    border: 1px solid rgba(0,0,0,0.1);
    border-radius: 10px;
    font-size: 16px;
    padding: 8px 0;
    text-indent: 15px;
    outline: none;
    resize: none;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
		Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}

.save-data-btn {
    width: 70%;
    padding: 0 0 20px 0;
    text-align: center;
}

.save-data-btn button {
    width: 100%;
    padding: 13px 45px;
    margin: 15px 0;
    background: #75a297;
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

.save-data-btn button:hover {
    background-color: rgb(95, 140, 128);
    color: rgba(255,255,255,0.8);
}

@media (max-width: 820px) {
    .login-card {
        width: 550px;
    }

    .info-area {
        flex: 2;
    }

    .table-area {
        flex: 3;
    }
}
@media (max-width: 600px) {
    .login-card {
        width: 80%;
        height: fit-content;
        flex-direction: column;
    }

    .info-area {
        flex: 2;
        align-items: center;
        justify-content: center;
        padding: 20px 0;
        height: auto;
    }

    .avatar-box {
        width: 60%;
    }

    .table-area {
        flex: 3;
        height: auto;
    }

    .table-row {
        width: 80%;
        min-height: 50px;
        padding: 30px 30px 20px 30px;
    }

    .row-name {
        width: 100%;
    }

    .row-data input,
    .row-data textarea {
        width: 100%;
    }

    .save-data-btn {
        width: 80%;
        padding: 0 30px 20px 30px;
    }
}
</style>
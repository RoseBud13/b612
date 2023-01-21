<template>
    <div class="home-navbar">
        <div class="navbar-container" :class="(dashboard? 'dashboard-shown' : '')">
            <div class="navbar-left">
                <port @goTo="toUniverse"></port>
            </div>
            <div class="navbar-mid">
                <div v-if="$route.name == 'home'" class="clock-box" @click="toggleDashboard(this.dashboard)" style="cursor: pointer;">
                    <clock :blink="true" :displaySeconds="false" :twelveHour="false"></clock>
                </div>
                <div v-else class="clock-box" >
                    <clock :blink="true" :displaySeconds="false" :twelveHour="false"></clock>
                </div>
            </div>
            <div class="navbar-right" :class="[theme]">
                <div v-if="$route.name == 'home'" class="menu-item">
                    <div class="menu-btn">
                        <i class="fas fa-cog"></i>
                    </div>
                    <ul class="menu-subitems">
                        <li @click="toggleHomeThemeWithPic(this.themeWithPic)">
                            <i v-if="theme === 'light'" class="fas fa-image"></i>
                            <i v-else-if="theme === 'dark'" class="fas fa-image"></i>
                            <i v-else class="fas fa-shapes"></i>
                        </li>
                        <li @click="toggleHomeTheme(this.icon)">
                            <i :class="['fas', `fa-${icon}`]"></i>
                        </li>
                    </ul>
                </div>
                <div v-else class="menu-item">
                    <div class="menu-btn">
                        <router-link to="/">
                            <i class="fas fa-home"></i>
                        </router-link>
                    </div>
                </div>
                <div class="menu-item">
                    <div class="menu-btn" v-if="!this.$store.state.authToken" @click="toggleLoginModal(this.showLogin)">
                        <i class="fas fa-user-circle"></i>
                    </div>
                    <div v-else>
                        <img
                            class="user-avatar"
                            :src="this.userAvatarUrl"
                            height="30"
                            width="30"
                        />
                        <ul class="menu-subitems">
                            <li v-if="$route.name != 'user'">
                                <router-link :to="this.userPageUrl">
                                    <i class="fas fa-user-circle"> 
                                        <p>个人中心</p>
                                    </i>
                                </router-link>
                            </li>
                            <li>
                                <div @click="handleLogout()">
                                    <i class="fas fa-sign-out-alt">
                                        <p>退出</p>
                                    </i>
                                </div>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { defineComponent } from 'vue'
import { mapMutations } from 'vuex';
import Port from './Port.vue';
import Clock from './widget/Clock.vue';

export default defineComponent({
    components: {
        Port,
        Clock
    },
    data() {
        return {
            icon: this.$store.state.homeThemeIcon,
            dashboard: this.$store.state.showDashboard,
            theme: this.$store.state.homeTheme,
            themeWithPic: this.$store.state.isHomeThemeWithPic,
            showLogin: this.$store.state.showLogin,
            userAvatarUrl: this.$store.state.userInfo.avatar? this.$store.state.userInfo.avatar : 'https://b612-static-rsrcs-1306125602.cos.ap-shanghai.myqcloud.com/user-avatar%2Fdefault-avatar.png',
            userPageUrl: '/user/' + this.$store.state.userInfo.username
        }
    },
    methods: {
        ...mapMutations(['toggleHomeTheme', 'toggleDashboard', 'toggleHomeThemeWithPic', 'toggleLoginModal', 'logout']),

        toUniverse() {
            this.$router.push({name: "universe"})
        },
        handleLogout() {
            this.logout();
            this.$toast('已驶离B612', 'success', 2000);
            setTimeout(() => {
                this.$router.push({name: "home"});
                location.reload();
            }, 1000)
        }
    },
    watch: {
        '$store.state.homeThemeIcon'(newVal, oldVal) {
            this.icon = newVal
            // console.log(this.icon)
        },
        '$store.state.showDashboard'(newVal, oldVal) {
            this.dashboard = newVal
            // console.log(this.dashboard)
        },
        '$store.state.homeTheme'(newVal, oldVal) {
            this.theme = newVal
            // console.log(this.theme)
        },
        '$store.state.isHomeThemeWithPic'(newVal, oldVal) {
            this.themeWithPic = newVal
            // console.log(this.themeWithPic)
            // console.log(this.theme)
        },
        '$store.state.showLogin'(newVal, oldVal) {
            this.showLogin = newVal
        },
        '$store.state.userInfo'(newVal, oldVal) {
            this.userPageUrl = '/user/' + newVal.username
        }
    }
})
</script>

<style lang="scss" scoped>
ul {
  list-style: none;
}
.home-navbar {
    position: absolute;
    top: 0;
    z-index: 100;
    width: 100vw;
    height: 50px;
}
.navbar-container {
    width: 100%;
    height: 100%;
    font-size: 17px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.dashboard-shown {
    backdrop-filter: blur(40px);
    -webkit-backdrop-filter: blur(40px);
}
.navbar-left {
    flex: 1;
    align-self: center;
}
.navbar-mid {
    flex: 2;
    align-self: center;
}
.navbar-right {
    flex: 1;
    align-self: center;
    display: flex;
    justify-content: flex-end;
}
.clock-box {
    margin: auto;
    width: 100%;
    height: 30px;
}
.menu-item {
    position: relative;
    width: 40px;
    height: 30px;
    line-height: 30px;
    text-align: center;
    margin: 0 10px 0 0;
    border-radius: 5px;
    cursor: pointer;
}
.user-avatar {
  cursor: pointer;
  border-radius: 50%;
}
.menu-item:hover .menu-btn i {
    color: #49b1f5;
}
.menu-subitems {
  position: absolute;
  display: none;
  right: 0;
  width: max-content;
  box-shadow: 0 5px 20px -4px rgba(0, 0, 0, 0.5);
  background-color: #fff;
  animation: showsub 0.3s 0.1s ease both;
}
.menu-subitems i {
    color: #23373d;
    margin: 12px 10px 12px 10px;
}
.menu-subitems i p {
    font-weight: 400;
    font-size: 0.9rem;
    display: inline;
    margin: 0 5px;
}
.menu-item:hover .menu-subitems {
  display: block;
}
.menu-subitems li:hover i {
    color: #49b1f5;
}
.dark .menu-btn i {
    color: #daf6ff;
}
.night .menu-btn i {
    color: #daf6ff;
}
.light .menu-btn i {
    color: #23373d;
}
.sunset .menu-btn i {
    color: #daf6ff;
}
@keyframes showsub {
  0% {
    opacity: 0;
    filter: alpha(opacity=0);
    transform: translateY(10px);
  }
  100% {
    opacity: 1;
    filter: none;
    transform: translateY(0);
  }
}
</style>

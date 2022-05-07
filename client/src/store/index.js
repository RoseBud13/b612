import {createStore} from 'vuex'

export default createStore({
    state: {
        continent:
        {
            name: '欢迎来到B612星球',
            spots: [
            {
                id: 1,
                title: '小王子的唱片机',
                icon: 'record-vinyl',
                color: 'pink',
                linkTo: 'http://www.b612.one/bubble-turntable'
            },
            {
                id: 2,
                title: '小王子的故事书',
                icon: 'book',
                color: 'pink',
                linkTo: 'http://www.b612.one/lp/index.pdf'
            },
            {
                id: 3,
                title: '旧版主页',
                icon: 'archive',
                color: 'pink',
                linkTo: 'http://www.b612.one/old'
            }
            ],
        },
        landed: null,
        departured: null,
        homeThemeIcon: 'sun',
        homeTheme: 'dark',
        showDashboard: false
    },
    mutations: {
        landedCon (state, landed) {
            state.departured = null
            state.landed = landed
        },
        departuredCon (state) {
            state.departured = state.landed
            state.landed = null
        },
        toggleHomeTheme (state, icon) {
            if (icon === 'sun') {
                state.homeThemeIcon = 'moon'
                state.homeTheme = 'light'
            } else {
                state.homeThemeIcon = 'sun'
                state.homeTheme = 'dark'
            }
        },
        toggleDashboard (state, dasboardStatus) {
            if (dasboardStatus === false) {
                state.showDashboard = true
            } else {
                state.showDashboard = false
            }
        }
    },
    actions: {},
    modules: {}
})

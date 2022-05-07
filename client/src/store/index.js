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
        homeTheme: 'night',
        showDashboard: false,
        isHomeThemeWithPic: true
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
                if (state.isHomeThemeWithPic === true) {
                    state.homeThemeIcon = 'moon'
                    state.homeTheme = 'sunset'
                } else {
                    state.homeThemeIcon = 'moon'
                    state.homeTheme = 'light'
                }
            } else {
                if (state.isHomeThemeWithPic === true) {
                    state.homeThemeIcon = 'sun'
                    state.homeTheme = 'night'
                } else {
                    state.homeThemeIcon = 'sun'
                    state.homeTheme = 'dark'
                }
            }
        },
        toggleDashboard (state, dasboardStatus) {
            if (dasboardStatus === false) {
                state.showDashboard = true
            } else {
                state.showDashboard = false
            }
        },
        toggleHomeThemeWithPic (state, homeThemeWithPic) {
            if (homeThemeWithPic === true) {
                state.isHomeThemeWithPic = false
                if (state.homeTheme === 'night') {
                    state.homeTheme = 'dark'
                } else {
                    state.homeTheme = 'light'
                }
            } else {
                state.isHomeThemeWithPic = true
                if (state.homeTheme === 'dark') {
                    state.homeTheme = 'night'
                } else {
                    state.homeTheme = 'sunset'
                }
            }
        }

    },
    actions: {},
    modules: {}
})

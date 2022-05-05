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
        universeThemeIcon: 'sun',
        universeTheme: 'dark',
        isDashboard: null
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
        toggleUniverseTheme (state, icon) {
            if (icon === 'sun') {
                state.universeThemeIcon = 'moon'
                state.universeTheme = 'light'
            } else {
                state.universeThemeIcon = 'sun'
                state.universeTheme = 'dark'
            }
        },
        toggleDashboard (state, dasboardStatus) {
            if (dasboardStatus === 'dashboard') {
                state.isDashboard = null
            } else {
                state.isDashboard = 'dashboard'
            }
        }
    },
    actions: {},
    modules: {}
})

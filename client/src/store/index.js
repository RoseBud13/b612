import {createStore} from 'vuex'
import { storage } from '../utils/storage'

export default createStore({
    state: {
        landed: null,
        departured: null,
        homeThemeIcon: 'sun',
        homeTheme: 'night',
        showDashboard: false,
        isHomeThemeWithPic: true,
        showLogin: false,
        authToken: storage.getAuthToken(),
        userInfo: storage.getAuthUserInfo(), // uid avatar username name
        localSettingInfo: storage.getLocalSettingInfo(),
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
        tasks: [
            {
                id: 3,
                title: 'Modify the homepage',
                date: new Date(),
                done: true,
                deleted: false
            },
            {
                id: 4,
                title: 'Add todo page',
                date: new Date(),
                done: true,
                deleted: false
            },
            {
                id: 5,
                title: 'Work out',
                date: new Date(),
                done: false,
                deleted: false
            },
            {
                id: 6,
                title: 'Weekly Report',
                date: new Date(),
                done: true,
                deleted: false
            },
            {
                id: 7,
                title: 'Deploy backend',
                date: new Date('2022-06-01'),
                done: false,
                deleted: false
            },    
            {
                id: 9,
                title: 'Braintorming',
                date: new Date('2022-05-16'),
                done: false,
                deleted: false
            },
            {
                id: 8,
                title: 'Food purchasing',
                date: new Date('2022-05-20'),
                done: false,
                deleted: false
            }
        ],
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
        },
        deleteTask(_, { task }) {
            task.deleted = true
        },
        addTask(state, newTask) {
            state.tasks.push(newTask)
        },
        toggleLoginModal(state, modalStatus) {
            if (modalStatus === false) {
                state.showLogin = true
            } else {
                state.showLogin = false
            }
        },
        login(state, data) {
            let localSetting = storage.getLocalSettingInfo();
            if (localSetting) {
                if (!localSetting.includes('loggedIn')) {
                    localSetting.push('loggedIn');
                }
            } else {
                localSetting = ['loggedIn'];
            }
            state.localSettingInfo = localSetting;
            storage.setLocalSettingInfo(localSetting);
            state.authToken = data.token;
            state.userInfo = data.userInfo;
            storage.setAuthToken(data.token);
            storage.setAuthUserInfo(data.userInfo);
        },
        logout(state) {
            state.authToken = null;
            state.userInfo = null;
            storage.removeAuthToken();
            storage.removeAuthUserInfo();
        },
        updateUserInfo(state, data) {
            state.userInfo = data;
            storage.setAuthUserInfo(data);
        },
    },
    getters: {
        todayTasks (state) {
            const tasks = []
            state.tasks.forEach(task => {
                if (task.date <= tomorrow && !task.done && !task.deleted) {
                    tasks.push(task)
                }
            })
            return tasks
        }
    },
    actions: {},
    modules: {}
})

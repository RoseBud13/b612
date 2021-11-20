import {createStore} from 'vuex'

export default createStore({
    state: {
        continent:
        {
            icon: 'user',
            name: 'B612',
            spots: [
            {
                id: 1,
                title: 'Turntabel',
            }
            ],
            colors: ['#ff6262', '#ffa947']
        },
        landed: null,
        departured: null,
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
    },
    actions: {},
    modules: {}
})

<template>
    <div class="dashboard" :class="(showDashboard? 'show' : '')">
        <div class="dashboard-container">
            <div class="widget-toggle" :class="[theme]" @click="toggleWidgets">
                widgets
            </div>
            <Transition name="widget-panel-show-hide">
                <div class="widget-panel" v-show="this.showWidgets === 'show'">
                    <div class="daily-update" :class="[theme]">
                        <div class="quote-content">
                            <div class="quote-text">{{ dailyQuote }}</div>
                            <div class="quote-info">{{ quoteInfo }}</div>
                        </div>
                        <div class="weather-report">
                            <div class="weather-date">{{ dateText }}</div>
                            <div class="weather-info">{{ weatherText }}</div>
                        </div>
                    </div>
                    <div class="widgets">
                        <div class="card">
                            <img :src="dailyPicUrl" alt="daily_pic">
                        </div>
                        <div class="card">
                            <iframe src="https://bubble-player-1306125602.cos-website.ap-shanghai.myqcloud.com" width="100%" height="200" style="border:none;"></iframe>
                        </div>
                        <div class="mini-card-wrapper">
                            <div class="mini-card">
                                <little-fox></little-fox>
                            </div>
                            <div class="mini-card">
                                <mini-slider></mini-slider>
                            </div>
                        </div>
                        <div class="card">
                            <iframe src="https://chrome-dino-1306125602.cos-website.ap-shanghai.myqcloud.com" width="100%" height="200" style="border:none;"></iframe>
                        </div>
                        <div class="mini-card-wrapper">
                            <div class="mini-card"></div>
                            <div class="mini-card"></div>
                        </div>
                        <div class="mini-card-wrapper">
                            <div class="mini-card"></div>
                        </div>
                    </div>
                </div>
            </Transition>
            <div class="app-panel">
                <div class="app-window">
                    <ul class="app-window-slides">
                        <input type="radio" id="app-window-control-1" name="control" checked>
                        <input type="radio" id="app-window-control-2" name="control">
                        <input type="radio" id="app-window-control-3" name="control">
                        <li class="app-window-slide-item">
                            <post-deck></post-deck>
                        </li>
                        <li class="app-window-slide-item">
                            <shelf-deck></shelf-deck>
                        </li>
                        <li class="app-window-slide-item">
                            to-do list
                        </li>
                    </ul>
                </div>
                <div class="apps">
                    <div class="apps-left">
                        <app-box></app-box>
                    </div>
                    <div class="apps-right">
                        <div class="app-window-view-controls">
                            <label for="app-window-control-1">
                                <i class="fas fa-comment-alt"></i>
                            </label>
                            <label for="app-window-control-2">
                                <i class="fas fa-bookmark"></i>
                            </label>
                            <label for="app-window-control-3">
                                <i class="fas fa-th-list"></i>
                            </label>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { defineComponent } from 'vue'
import { getOneQuote } from "../api"
import LittleFox from "../components/LittleFox.vue"
import MiniSlider from "../components/MiniSlider.vue"
import PostDeck from './PostDeck.vue'
import ShelfDeck from './ShelfDeck.vue'
import AppBox from './AppBox.vue'

export default defineComponent({
    components: {
        LittleFox,
        MiniSlider,
        PostDeck,
        ShelfDeck,
        AppBox
    },
    data() {
        return {
            showDashboard: this.$store.state.showDashboard,
            theme: this.$store.state.homeTheme,
            dailyQuote: '',
            quoteInfo: '',
            dateText: '',
            weatherText: '',
            dailyPicUrl: '',
            showWidgets: ''
        }
    },
    watch: {
        '$store.state.showDashboard'(newVal, oldVal) {
            this.showDashboard = newVal
            // console.log(this.showDashboard)
        },
        '$store.state.homeTheme'(newVal, oldVal) {
            this.theme = newVal
            // console.log(this.theme)
        },
    },
    methods: {
        getDailyQuote() {
            getOneQuote().then(res => {
                this.dailyQuote = res.data.data.content_list[0].forward
                this.quoteInfo = '—— ' + res.data.data.content_list[0].words_info
                this.dateText = res.data.data.weather.date.slice(0,4) + '年' + res.data.data.weather.date.slice(5,7) + '月' + res.data.data.weather.date.slice(8) + '日'
                this.weatherText = res.data.data.weather.city_name + ' ' + '平流层 ' + ' 温度 ' + '-57.15°C'
                this.dailyPicUrl = 'https://b612.one/daily/img/' + res.data.data.content_list[0].img_url.slice(27)
                console.log(this.dailyQuote)
            }).catch(e => {
                console.log(e)
            })
        },
        setWidgetsShow() {
            let width = Math.max(window.screen.width, window.innerWidth);
            if (width > '820') {
                this.showWidgets = 'show'
            } else {
                this.showWidgets = 'hide'
            }
        },
        toggleWidgets() {
            if (this.showWidgets === 'show') {
                this.showWidgets = 'hide'
            } else {
                this.showWidgets = 'show'
            }
        }
        // getDeviceHeight() {
        //     // Update the element's size
        //     let vh = window.innerHeight * 0.01;
        //     document.documentElement.style.setProperty('--vh', `${vh}px`);
        // }
    },
    mounted() {
        this.getDailyQuote()
        this.setWidgetsShow()
        // this.getDeviceHeight()
    }
})
</script>

<style lang="scss" scoped>
.dashboard {
    position: absolute;
    bottom: 0;
    width: 100%;
    height: 0;

    z-index: 1;
    transition: all 1.2s ease-in-out;
}
.dashboard-container {
    width: 100%;
    // height: calc(100% - 50px);
    height: 100%;
    // color: rgb(255, 255, 255);
    // margin-top: 50px;
    display: flex;

    // * {
    //     // border: 1px solid black;
    //     background-color: #eee;
    // }
}
.dashboard-container::-webkit-scrollbar {
    display: none;
}
.widget-toggle {
    width: 100%;
    height: 1.1rem;
    margin: 10px 0 0 0;
    display: none;

    text-align: center;
    font-size: 0.9rem;
    font-weight: lighter;
}
.widget-panel {
    flex: 3;
    
    display: flex;
    flex-direction: column;
}
.widget-panel-show-hide-enter-active,
.widget-panel-show-hide-leave-active {
  transition: opacity 0.3s ease;
}
.widget-panel-show-hide-enter-from,
.widget-panel-show-hide-leave-to {
  opacity: 0;
}
.app-panel {
    flex: 7;
    display: flex;
    flex-direction: column;
    // * {
    //     border: 1px solid black;
    //     background-color: #eee;
    // }
}
.daily-update {
    background-color: rgba(255, 255, 255, 0);
    height: 150px;
    max-width: 550px;
    margin: 15px 25px;
    border-radius: 30px;

    display: flex;
    flex-direction: column;
}
.quote-content {
    margin: 15px 25px;
    display: flex;
    flex-direction: column;
}
.quote-text {
    font-size: 1rem;
}
.quote-info {
    font-size: 0.7rem;
    margin-top: 5px;
    align-self: flex-end;
}
.weather-report {
    margin: 8px 25px;
    display: flex;
    justify-content: flex-end;

    margin-top: auto;
}
.weather-date {
    margin: 0 10px;
    font-size: 0.8rem;
}
.weather-info {
    margin: 0 10px;
    font-size: 0.8rem;
}
.widgets {
    overflow: auto;

    padding-bottom: 20px;

    flex: 1;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}
.widgets::-webkit-scrollbar {
    display: none;
}
.card {
    background-color: rgba(255, 255, 255, 0.7);
    width: 100%;
    height: 200px;
    max-width: 550px;
    min-height: 200px;
    margin: 25px 25px 0 25px;
    border-radius: 30px;
}
.card img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
    border-radius: inherit;
}
.mini-card-wrapper {
    background-color: rgba(255, 255, 255, 0);
    width: 100%;
    height: 250px;
    max-width: 550px;
    margin: 25px 25px 0 25px;
    border-radius: 30px;
    display: flex;
    justify-content: space-between;
}
.mini-card {
    background-color: rgba(255, 255, 255, 0.7);
    width: 250px;
    height: 250px;
    margin: 0;
    border-radius: 30px;
}

.card iframe {
    border-radius: 30px;
}

.app-window {
    flex: 5;

    margin: 15px 25px 0 25px;
    min-height: 429px;
}
.app-window-slides {
    position: relative;
    width: 100%;
    height: 100%;
    list-style: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
}
.app-window-slide-item {
    margin: 0;
    padding: 0;
    width: inherit;
    height: inherit;
    position: absolute;
    top: 0;
    left: 0;
    overflow-y: auto;
    overflow-x: hidden;

    transition: .5s transform ease-in-out;
}
.app-window-slide-item::-webkit-scrollbar {
    display: none;
}

.app-window-slide-item:nth-of-type(1) {
    left: 0;
}
.app-window-slide-item:nth-of-type(2) {
    left: 100%;
}
.app-window-slide-item:nth-of-type(3) {
    left: 200%;
}

input[type="radio"] {
    position: relative;
    display: none;
}

.app-window-slides input[type="radio"]:nth-of-type(1):checked ~ .app-window-slide-item {
//   transform: translatex(0%);
    transform: none;
}

.app-window-slides input[type="radio"]:nth-of-type(2):checked ~ .app-window-slide-item {
    transform: translatex(-100%);
}

.app-window-slides input[type="radio"]:nth-of-type(3):checked ~ .app-window-slide-item {
    transform: translatex(-200%);
}

.apps {
    flex: 2;

    display: flex;
    margin: 15px 25px;
    max-height: 45%;
    min-height: 240px;
}
.apps-left {
    flex: 1;

    padding: 10px 15px 0 15px;
    overflow: auto;
}
.apps-left::-webkit-scrollbar {
    display: none;
}
.apps-right {
    flex: 1;

    padding: 15px;
}

.app-window-view-controls {
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: space-around;
    align-items: center;
    flex-wrap: wrap;

}
.app-window-view-controls label {
    display: block;
    width: 75px;
    height: 75px;
    border-radius: 23%;
    margin: 20px;
    background-color: #fff;
    
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 2rem;
}
.app-window-view-controls label i {
    color: #23373d;
}

.show {
    // height: calc(var(--vh, 1vh) * 100 - 50px);
    height: 100%;
}

.dark .quote-content {
    color: #eee;
}
.night .quote-content {
    color: #eee;
}
.light .quote-content {
    color: #23373d;
}
.sunset .quote-content {
    color: #eee;
}
.dark .weather-report {
    color: #eee;
}
.night .weather-report {
    color: #eee;
}
.light .weather-report {
    color: #23373d;
}
.sunset .weather-report {
    color: #eee;
}
.dark .widget-toggle {
    color: #eee;
}
.night .widget-toggle {
    color: #eee;
}
.light .widget-toggle {
    color: #23373d;
}
.sunset .widget-toggle {
    color: #eee;
}

@media (max-width: 1440px) {
    .card {
        height: 180px;
        min-height: 180px;
    }
    .card iframe {
        height: 180px;
        overflow: hidden;
    }
    .mini-card-wrapper {
        height: 170px;
    }
    .mini-card {
        width: 170px;
        height: 170px;
    }
}
@media (max-width: 820px) {
    .dashboard-container {
        flex-direction: column;
        overflow: auto;
    }
    .widget-toggle {
        display: block;
    }
    .widget-panel {
        width: 100%;
    }
    .daily-update {
        max-width: 100%;
        margin: 15px 100px;
    }
    .widgets {
        flex-direction: column;
    }
    .card {
        max-width: 75%;
        margin: 25px auto 0 auto;
    }
    .mini-card-wrapper {
        max-width: 75%;
        margin: 25px auto 0 auto;
        height: 32vw;
    }
    .mini-card {
        width: 32vw;
        height: 32vw;
    }
    // .app-panel {
    //     display: none;
    // }
}
@media (max-width: 600px) {
    .dashboard-container {
        overflow: auto;
    }
    .widget-panel {
        width: 100%;
    }
    .dashboard-container {
        flex-direction: column;
    }
    .daily-update {
        max-width: 100%;
        margin: 15px 10px;
    }
    .widgets {
        flex-direction: column;
    }
    .card {
        max-width: 85%;
    }
    .mini-card-wrapper {
        max-width: 85%;
        height: 40vw;
    }
    .mini-card {
        width: 40vw;
        height: 40vw;
    }
    // .app-panel {
    //     display: none;
    // }
}
</style>

<template>
    <div class="dashboard" :class="(showDashboard? 'show' : '')">
        <div class="dashboard-container">
            <div class="widget-box">
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
            <div class="app-box">
                <div class="app-window"></div>
                <div class="apps">
                    <div class="apps-left">
                        <div class="icon-container logo-color-bili">
                            <a href="https://bilibili.com" target="_blank">
                                <img src="../assets/img/logo/bilibili.svg" alt="Bilibili" class="svg-fillter-bili">
                            </a>
                        </div>
                        <div class="icon-container logo-color-gh">
                            <a href="https://github.com" target="_blank">
                                <img src="../assets/img/logo/github.svg" alt="GitHub">
                            </a>
                        </div>
                        <div class="icon-container logo-color-weibo">
                            <a href="https://weibo.com" target="_blank">
                                <img src="../assets/img/logo/sinaweibo.svg" alt="Weibo" class="svg-fillter-weibo">
                            </a>
                        </div>
                        <div class="icon-container logo-color-douban">
                            <a href="https://douban.com" target="_blank">
                                <img src="../assets/img/logo/douban.svg" alt="Douban" class="svg-fillter-douban">
                            </a>
                        </div>
                        <div class="icon-container logo-color-zhihu">
                            <a href="https://zhihu.com" target="_blank">
                                <img src="../assets/img/logo/zhihu.svg" alt="Zhihu" class="svg-fillter-zhihu">
                            </a>
                        </div>
                        <div class="icon-container logo-color-yt">
                            <a href="https://youtube.com" target="_blank">
                                <img src="../assets/img/logo/youtube.svg" alt="YouTube" class="svg-fillter-yt">
                            </a>
                        </div>
                        <div class="icon-container logo-color-notion">
                            <a href="https://notion.so" target="_blank">
                                <img src="../assets/img/logo/notion.svg" alt="Notion">
                            </a>
                        </div>
                    </div>
                    <div class="apps-right"></div>
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

export default defineComponent({
    components: {
        LittleFox,
        MiniSlider
    },
    data() {
        return {
            showDashboard: this.$store.state.showDashboard,
            theme: this.$store.state.homeTheme,
            dailyQuote: '',
            quoteInfo: '',
            dateText: '',
            weatherText: '',
            dailyPicUrl: ''
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
        getDeviceHeight() {
            // Update the element's size
            let vh = window.innerHeight * 0.01;
            document.documentElement.style.setProperty('--vh', `${vh}px`);
        }
    },
    mounted() {
        this.getDailyQuote()
        this.getDeviceHeight()
    }
})
</script>

<style lang="scss">
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
    color: rgb(255, 255, 255);
    // margin-top: 50px;
    display: flex;

    // * {
    //     // border: 1px solid black;
    //     background-color: #eee;
    // }
}
.widget-box {
    flex: 3;
    
    display: flex;
    flex-direction: column;
}
.app-box {
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
    font-size: 0.9rem;
}
.weather-info {
    margin: 0 10px;
    font-size: 0.9rem;
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
// .img-card {
//     background-image: url(../assets/img/bili.webp);
//     background-size: cover;
//     background-position: center;
// }
.app-window {
    flex: 6;

    margin: 15px 25px 0 25px;
}
.apps {
    flex: 5;

    display: flex;
    margin: 15px 25px;
    max-height: 45%;
}
.apps-left {
    flex: 1;

    display: flex;
    flex-wrap: wrap;
    align-content: flex-end;
    padding: 15px;
    overflow: auto;
}
.apps-left::-webkit-scrollbar {
    display: none;
}
.apps-right {
    flex: 1;

    display: flex;
    padding: 10px;
}
.icon-container {
    width: 75px;
    height: 75px;
    border-radius: 23%;
    margin: 20px;
    position: relative;
}
.icon-container img {
    position: absolute; 
    top: 50%; 
    left: 50%;
    transform: translate(-50%, -50%);
    width: 70%;
}

.show {
    height: calc(var(--vh, 1vh) * 100 - 50px);
    //height: calc(100vh - 50px);
}

.logo-color-bili {
    background-color: #5bc9e0;
}
.logo-color-gh {
    background-color: #fff;
}
.logo-color-weibo {
    background-color: #df2029;
}
.logo-color-douban {
    background-color: #2e963d;
}
.logo-color-zhihu {
    background-color: #fff;
    img {
        width: 100%;
    }
}
.logo-color-yt {
    background-color: #fff;
}
.logo-color-notion {
    background-color: #fbf3da;
}
.svg-fillter-bili {
    filter: invert(100%) sepia(0%) saturate(7500%) hue-rotate(304deg) brightness(106%) contrast(106%);
}
.svg-fillter-weibo {
    filter: invert(100%) sepia(0%) saturate(7500%) hue-rotate(304deg) brightness(106%) contrast(106%);
}
.svg-fillter-douban {
    filter: invert(100%) sepia(0%) saturate(7500%) hue-rotate(304deg) brightness(106%) contrast(106%);
}
.svg-fillter-zhihu {
    filter: invert(41%) sepia(98%) saturate(4538%) hue-rotate(191deg) brightness(107%) contrast(89%);
}
.svg-fillter-yt {
    filter: invert(23%) sepia(91%) saturate(7027%) hue-rotate(357deg) brightness(92%) contrast(115%);
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
    .icon-container {
        margin: 15px;
    }
}
@media (max-width: 820px) {
    .dashboard-container {
        overflow: auto;
    }
    .widget-box {
        width: 100%;
    }
    .dashboard-container {
        flex-direction: column;
    }
    .widgets {
        flex-direction: column;
    }
    .card {
        width: auto;
    }
    .mini-card-wrapper {
        width: auto;
        height: 32vw;
    }
    .mini-card {
        width: 32vw;
        height: 32vw;
    }
    .app-box {
        display: none;
    }
}
@media (max-width: 600px) {
    .dashboard-container {
        overflow: auto;
    }
    .widget-box {
        width: 100%;
    }
    .dashboard-container {
        flex-direction: column;
    }
    .widgets {
        flex-direction: column;
    }
    .card {
        width: auto;
    }
    .mini-card-wrapper {
        width: auto;
        height: 40vw;
    }
    .mini-card {
        width: 40vw;
        height: 40vw;
    }
    .app-box {
        display: none;
    }
}
</style>

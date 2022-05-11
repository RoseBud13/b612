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
                <div class="apps"></div>
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
    width: 600px;
    
    display: flex;
    flex-direction: column;
}
.app-box {
    flex: 1;
    display: flex;
    flex-direction: column;
    // * {
    //     // border: 1px solid black;
    //     background-color: #eee;
    // }
}
.daily-update {
    background-color: rgba(255, 255, 255, 0);
    height: 150px;
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
    font-size: 1em;
}
.quote-info {
    font-size: 10px;
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
    font-size: 13px;
}
.weather-info {
    margin: 0 10px;
    font-size: 13px;
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
    width: 550px;
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
    width: 550px;
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

.show {
    height: calc(var(--vh, 1vh) * 100 - 50px);
    //height: calc(100vh - 50px);
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
}
</style>

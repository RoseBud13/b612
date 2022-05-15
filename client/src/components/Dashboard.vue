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
                <div class="app-window">
                    <ul class="app-window-slides">
                        <input type="radio" id="app-window-control-1" name="control" checked>
                        <input type="radio" id="app-window-control-2" name="control">
                        <input type="radio" id="app-window-control-3" name="control">
                        <li class="app-window-slide-item">
                            <div class="masonry-view">
                                <div class="masonry-item">
                                    <img src="https://picsum.photos/360/400?random=1" alt="pic">
                                </div>
                                <div class="masonry-item">
                                    <img src="https://picsum.photos/360/480?random=2" alt="pic">
                                </div>
                                <div class="masonry-item">
                                    <img src="https://picsum.photos/360/420?random=3" alt="pic">
                                </div>
                                <div class="masonry-item">
                                    <img src="https://picsum.photos/360/500?random=4" alt="pic">
                                </div>
                                <div class="masonry-item">
                                    <img src="https://picsum.photos/360/480?random=5" alt="pic">
                                </div>
                                <div class="masonry-item">
                                    <img src="https://picsum.photos/360/500?random=6" alt="pic">
                                </div>
                                <div class="masonry-item">
                                    <img src="https://picsum.photos/360/400?random=7" alt="pic">
                                </div>
                                <div class="masonry-item">
                                    <img src="https://picsum.photos/360/440?random=8" alt="pic">
                                </div>
                                <div class="masonry-item">
                                    <img src="https://picsum.photos/360/460?random=9" alt="pic">
                                </div>
                                <div class="masonry-item">
                                    <img src="https://picsum.photos/360/500?random=10" alt="pic">
                                </div>
                                <div class="masonry-item">
                                    <img src="https://picsum.photos/360/420?random=11" alt="pic">
                                </div>
                                <div class="masonry-item">
                                    <img src="https://picsum.photos/360/480?random=12" alt="pic">
                                </div>
                                <div class="masonry-item">
                                    <img src="https://picsum.photos/360/400?random=13" alt="pic">
                                </div>
                                <div class="masonry-item">
                                    <img src="https://picsum.photos/360/500?random=14" alt="pic">
                                </div>
                                <div class="masonry-item">
                                    <img src="https://picsum.photos/360/480?random=15" alt="pic">
                                </div>
                                <div class="masonry-item">
                                    <img src="https://picsum.photos/360/480?random=16" alt="pic">
                                </div>
                            </div>
                        </li>
                        <li class="app-window-slide-item">
                            <div class="shelf-view">
                                <div class="shelf-items">
                                    <div class="shelf-upper">
                                        <div class="book-item">
                                            <img src="../assets/img/book_cover.jpeg" alt="book">
                                        </div>
                                        <div class="book-item">
                                            <img src="../assets/img/book_cover.jpeg" alt="book">
                                        </div>
                                        <div class="book-item">
                                            <img src="../assets/img/book_cover.jpeg" alt="book">
                                        </div>
                                        <div class="book-item">
                                            <img src="../assets/img/book_cover.jpeg" alt="book">
                                        </div>
                                        <div class="book-item">
                                            <img src="../assets/img/book_cover.jpeg" alt="book">
                                        </div>
                                        <div class="book-item">
                                            <img src="../assets/img/book_cover.jpeg" alt="book">
                                        </div>
                                        <div class="book-item">
                                            <img src="../assets/img/book_cover.jpeg" alt="book">
                                        </div>
                                        <div class="book-item">
                                            <img src="../assets/img/book_cover.jpeg" alt="book">
                                        </div>
                                    </div>
                                    <div class="shelf-lower">
                                        <div class="film-item">
                                            <img src="http://image.tmdb.org/t/p/w500//aKCvdFFF5n80P2VdS7d8YBwbCjh.jpg" alt="film">
                                        </div>
                                        <div class="film-item">
                                            <img src="http://image.tmdb.org/t/p/w500//aKCvdFFF5n80P2VdS7d8YBwbCjh.jpg" alt="film">
                                        </div>
                                        <div class="film-item">
                                            <img src="http://image.tmdb.org/t/p/w500//aKCvdFFF5n80P2VdS7d8YBwbCjh.jpg" alt="film">
                                        </div>
                                        <div class="film-item">
                                            <img src="http://image.tmdb.org/t/p/w500//aKCvdFFF5n80P2VdS7d8YBwbCjh.jpg" alt="film">
                                        </div>
                                        <div class="film-item">
                                            <img src="http://image.tmdb.org/t/p/w500//aKCvdFFF5n80P2VdS7d8YBwbCjh.jpg" alt="film">
                                        </div>
                                        <div class="film-item">
                                            <img src="http://image.tmdb.org/t/p/w500//aKCvdFFF5n80P2VdS7d8YBwbCjh.jpg" alt="film">
                                        </div>
                                        <div class="film-item">
                                            <img src="http://image.tmdb.org/t/p/w500//aKCvdFFF5n80P2VdS7d8YBwbCjh.jpg" alt="film">
                                        </div>
                                        <div class="film-item">
                                            <img src="http://image.tmdb.org/t/p/w500//aKCvdFFF5n80P2VdS7d8YBwbCjh.jpg" alt="film">
                                        </div>
                                    </div>
                                </div>
                                <div class="shelf-item-detail">
                                    <div class="item-wrapper">
                                        <img src="../assets/img/book_cover.jpeg" alt="book">
                                        <div class="item-title">
                                            <p>The Perks of Being a Wallflower</p>
                                        </div>
                                        <div class="item-content">
                                            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Inventore vitae, iusto sed explicabo dolores consequatur pariatur, rerum tempora illo provident ad necessitatibus consectetur atque culpa itaque maxime delectus iste corrupti.</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </li>
                        <li class="app-window-slide-item">
                            to-do list
                        </li>
                    </ul>
                </div>
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
  transform: translatex(0%);
}

.app-window-slides input[type="radio"]:nth-of-type(2):checked ~ .app-window-slide-item {
  transform: translatex(-100%);
}

.app-window-slides input[type="radio"]:nth-of-type(3):checked ~ .app-window-slide-item {
  transform: translatex(-200%);
}

.masonry-view {
    column-count: 5;
    column-gap: 0;
}
.masonry-item {
    padding: 4px;
}
.masonry-item img {
    display: block;
    width: 100%;
    height: auto;
    border-radius: 10px;
}
.shelf-view {
    display: flex;
    // flex-direction: column;
    width: 100%;
    height: 100%;

    // * {
    //     border: 1px solid black;
    //     background-color: #eee;
    // }
}
.shelf-items {
    flex: 1;

    display: flex;
    flex-direction: column;
    max-width: calc(100% - 320px);
    height: 100%;
}
.shelf-item-detail {
    min-width: 320px;
    width: 320px;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}
.shelf-upper {
    flex: 1;

    display: flex;
    align-items: center;
    overflow-x: auto;
    height: 100%;
}
.shelf-upper::-webkit-scrollbar {
    display: none;
}
.book-item {
    height: 60%;
    aspect-ratio: 6 / 7;
    margin: 0 0 0 30px;
    background-color: rgba(137, 210, 235, 0.7);
    border-radius: 13%;

    display: flex;
    justify-content: center;
    align-items: center;
}
.book-item img {
    height: 70%;
    border-radius: 13%;
}
.shelf-lower {
    flex: 1;

    display: flex;
    align-items: center;
    overflow-x: auto;
    height: 100%;
}
.shelf-lower::-webkit-scrollbar {
    display: none;
}
.film-item {
    height: 60%;
    aspect-ratio: 6 / 7;
    margin: 0 0 0 30px;
    background-color: rgba(170, 235, 137, 0.7);
    border-radius: 13%;

    display: flex;
    justify-content: center;
    align-items: center;
}
.film-item img {
    height: 70%;
    border-radius: 13%;
}
.item-wrapper {
    height: 90%;
    width: 100%;
    background-color: rgba(137, 210, 235, 1);
    text-align: center;
    border-radius: 20px;
}
.item-wrapper img {
    height: 40%;
    margin: 10px;
}
.item-title {
    margin-top: 20px;
}
.item-title p {
    font-size: 1.1rem;
    color: #fff;
}
.item-content {
    margin: 20px 15px;
    padding: 10px;
    text-align: justify;
}
.item-content p {
    font-size: 0.9rem;
    color: #fff;
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

    display: flex;
    flex-wrap: wrap;
    // align-content: flex-end;
    padding: 15px;
    overflow: auto;
}
.apps-left::-webkit-scrollbar {
    display: none;
}
.apps-right {
    flex: 1;

    padding: 15px;
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
.app-window-view-controls {
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: space-around;
    align-items: center;

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
    .shelf-items {
        max-width: calc(100% - 280px);
    }
    .shelf-item-detail {
        min-width: 280px;
        width: 280px;
    }
    .item-wrapper img {
        height: 35%;
        margin: 10px;
    }
    .item-title {
        margin-top: 10px;
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

<template>
    <div class="sun-moon" @dblclick="toggleSearchArea">
        <div id="sun-moon-container" :class="[theme]">
            <div class="bg"></div>
            <div class="moon-box">
                <div class="moon"></div>
            </div>
            <div class="sun-box">
                <div class="sun"></div>
            </div>
        </div>
        <Transition name="search-area-show">
            <div class="search-area" v-show="showSearchArea">
                <search-box></search-box>
            </div>
        </Transition>
    </div>
</template>

<script>
import { defineComponent } from 'vue'
import SearchBox from './SearchBox.vue'

export default defineComponent({
    components: {
        SearchBox
    },
    data() {
        return {
            theme: this.$store.state.homeTheme,
            showSearchArea: false
        }
    },
    watch: {
        '$store.state.homeTheme'(newVal, oldVal) {
            this.theme = newVal
            // console.log(this.theme)
        }
    },
    methods: {
        toggleSearchArea() {
            this.showSearchArea = !this.showSearchArea
        }
    }
})
</script>

<style lang="scss">
.sun-moon {
    z-index: -1;
}
#sun-moon-container {
    height: 100vh;
}
.search-area {
    position: absolute;
    top: 40%;
    left: 50%;
    transform: translateX(-50%);
}
.search-area-show-enter-active,
.search-area-show-leave-active {
  transition: opacity 0.5s ease;
}

.search-area-show-enter-from,
.search-area-show-leave-to {
  opacity: 0;
}
.bg{
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}
.sun{
    margin: 0;
    padding: 0;
    position: absolute;
    top: 55%;
    left: 50%;
    transform: translate(-50%,-50%);
    // width: 600px;
    // height: 600px;
    width: 25vw;
    height: 25vw;
    background-color: orange;
    border-radius: 50%;
}
.moon{
    margin: 0;
    padding: 0;
    position: absolute;
    // top: 50%;
    left: 50%;
    top: 55%;
    /* 计算得出月亮的位置 */
    // transform: translate(calc(-50% + -160px), calc(-50% + -180px));
    transform: translate(calc(-50% + -0.27*25vw), calc(-50% + -0.3*25vw));
    // width: 600px;
    // height: 600px;
    width: 25vw;
    height: 25vw;
    /* 通过阴影绘制月亮 */
    // box-shadow: 160px 180px 0 cyan;
    box-shadow: 0.27*25vw 0.3*25vw 0 cyan;
    border-radius: 50%;
}

/* 动画 */
.sun,
.moon,
.sun-box,
.moon-box,
.bg{
    /* 添加动画过渡 */
    transition: all 1s ease-in-out;
}

.sun-box,
.moon-box{
    /* 相对定位 */
    position: relative;
    /* 溢出隐藏 */
    overflow: hidden;
}

/* Light */
.light .sun-box{
    height: 100%;
}
.light .moon-box{
    height: 0;
}
.light .bg{
    background-color: #ffeea2;
}

/* Dark */
.dark .sun-box{
    height: 0;
}
.dark .moon-box{
    height: 100%;
}
.dark .bg{
    background-color: #040720;
}

/* 日落 */
.sunset .sun-box{
    height: 0;
}
.sunset .moon-box{
    height: 0;
}
.sunset .bg{
    background-color: #ffeea2;
    background-image: url(../assets/img/sunset.webp);
    background-size: cover;
    background-position: center;
}

/* 夜晚 */
.night .sun-box{
    height: 0;
}
.night .moon-box{
    height: 0;
}
.night .bg{
    background-color: #040720;
    background-image: url(../assets/img/night.webp);
    background-size: cover;
    background-position: center;
}

@media (max-width: 1000px) {
    .sun {
        top: 60%;
        width: 60vw;
        height: 60vw;
    }
    .moon {
        top: 60%;
        width: 60vw;
        height: 60vw;
        transform: translate(calc(-50% + -0.27*60vw), calc(-50% + -0.3*60vw));
        box-shadow: 0.27*60vw 0.3*60vw 0 cyan;
    }
}
</style>

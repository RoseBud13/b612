<template>
    <div class="sun-moon">
        <div id="sun-moon-container" :class="[theme, isDashboard]">
            <div class="bg"></div>
            <div class="moon-box">
                <div class="moon"></div>
            </div>
            <div class="sun-box">
                <div class="sun"></div>
            </div>
            <!-- <div class="sea"></div> -->
            <sea class="sea"></sea>
        </div>
    </div>
</template>

<script>
import Sea from "./Sea.vue"

export default {
    components: {
        Sea
    },
    data() {
        return {
            theme: this.$store.state.homeTheme,
            isDashboard: this.$store.state.isDashboard
        }
    },
    watch: {
        '$store.state.homeTheme'(newVal, oldVal) {
            this.theme = newVal
            // console.log(this.theme)
        },
        '$store.state.isDashboard'(newVal, oldVal) {
            this.isDashboard = newVal
            // console.log(this.isDashboard)
        },
    }
}
</script>

<style lang="scss">
.sun-moon {
    z-index: -1;
}
#sun-moon-container {
    height: 100vh;
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
.sea {
    transition: all 1.2s ease-in-out;
}

.sun-box,
.moon-box{
    /* 相对定位 */
    position: relative;
    /* 溢出隐藏 */
    overflow: hidden;
}

/* 白天 */
.light .sun-box{
    height: 100%;
}
.light .moon-box{
    height: 0;
}
.light .bg{
    background-color: #ffeea2;
}

/* 夜晚 */
.dark .sun-box{
    height: 0;
}
.dark .moon-box{
    height: 100%;
}
.dark .bg{
    background-color: #040720;
}

/* 工作区 */
.dashboard .sea {
    height: 100%;
    backdrop-filter: blur(40px);
    -webkit-backdrop-filter: blur(40px);
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

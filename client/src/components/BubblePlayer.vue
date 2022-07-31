<template>
    <div class="player">
        <div class="disk-wrapper">
            <div class="disk" :class="{ disk__playing: isPlaying }">
                <label 
                    class="disk-cover" 
                    ref="cover"
                    :style="{
                        transform: stopMatrix,
                    }"
                ></label>
            </div>
        </div>
        <div class="control-buttons-wrapper">
            <div class="control" :class="{ control__playing: isPlaying }">
                <div class="button" v-if="!isPlaying" @click="play()">
                    <i class="fas fa-play"></i>
                </div>
                <div class="button" v-else @click="pause()">
                    <i class="fas fa-pause"></i>
                </div>
            </div>
        </div>
    </div>
    <div class="progress-bar-wrapper">
        <div class="progress" :class="{ progress__playing: isPlaying }">
            <h2 class="progress-title">{{ audioInfo.title }}</h2>
            <p class="progress-text">
                {{ currentTimer }} / {{ totalTimer }}
            </p>
            <div class="bar">
                <span :style="{ width: progress }"></span>
            </div>
        </div>
    </div>
</template>

<script>
import { defineComponent } from "vue"
import { timeFormater } from "../utils/timer"

export default defineComponent({
    props: {
        audioInfo: {
            type: Object,
            default: {}
        }
    },
    data() {
        return {
            isPlaying: false,
            player: new Audio(),
            currentTimer: '00:00',
            totalTimer: '',
            progress: '',
            stopMatrix: ''
        }
    },
    mounted() {
        this.setAudio();
        
        const draw = () => {
            requestAnimationFrame(draw);
            const progress = this.player.currentTime / this.audioInfo.seconds;
            this.progress = `${(progress * 100).toFixed(2)}%`;
        };
        draw();
    },
    methods: {
        setAudio() {
            this.player.src = this.audioInfo.src;
            this.totalTimer = timeFormater(this.audioInfo.seconds);
        },

        playListener() {
            this.player.addEventListener("timeupdate", () => {
                let playerTimer = this.player.currentTime;

                this.currentTimer = timeFormater(playerTimer);
                // this.isPlaying = true;
            });
            this.player.addEventListener("ended", () => {
                this.isPlaying = false;
                this.player.currentTime = 0;
                // this.player.pause();
            });
        },

        play() {
            this.player.play();
            this.isPlaying = true;
            this.playListener();
        },

        pause() {
            this.player.pause();
            this.isPlaying = false;
        },
    },
    watch: {
        // $route(to, from){
        //     this.isPlaying = false;
        //     this.player.pause();
        // },

        isPlaying(newVal, oldVal) {
            if (!newVal) {
                this.stopMatrix = window.getComputedStyle(this.$refs.cover).transform;
            } else {
                const matrix = this.stopMatrix;
                this.stopMatrix = "";
                const match = matrix.match(/^matrix\(([^,]+),([^,]+)/);
                const [, sin, cos] = match || [0, 0, 0];
                const deg = ((Math.atan2(cos, sin) / 2 / Math.PI) * 360) % 360;
                const styles = [...document.styleSheets];
                styles.forEach((style) => {
                    const rules = [...style.cssRules];
                    rules.forEach((rule) => {
                        if (rule.type === rule.KEYFRAMES_RULE && rule.name === "rotate") {
                        rule.cssRules[0].style.transform = `rotate(${deg}deg)`;
                        rule.cssRules[1].style.transform = `rotate(${deg + 360}deg)`;
                        }
                    });
                });
            }
        },
    },
})
</script>

<style lang="scss" scoped>
.player {
    // position: absolute;
    // top: 0;
    display: flex;
    margin-top: 40px;
    margin-bottom: 60px;
    max-width: 300px;
    max-height: 75px;
    width: 300px;
    height: 75px;
    border-radius: 8px;
    background-color: white;
    box-shadow: 0 30px 60px rgba(0, 0, 0, 0.12),
        0 20px 20px rgba(95, 23, 101, 0.2);
    z-index: 99;
}
.disk-wrapper {
    flex: 1.2;
    padding: 12px;
}
.control-buttons-wrapper {
    flex: 2;
    padding: 12px 0;
    padding-right: 12px;
}
.progress-bar-wrapper {
    position: absolute;
    top: 0;
    margin-top: 40px;
    width: 282px;
    height: 50px;
    z-index: 98;
}

.disk {
    position: relative;
    padding-top: 100%;
    border-radius: 100%;
    overflow: hidden;
    transform: translateY(-50%) scale(0.88);
    transform-origin: center bottom;
    transition: all 0.6s ease;
}
.disk-cover {
    position: absolute;
    top: -10px;
    left: -10px;
    right: -10px;
    bottom: -10px;
    background-image: radial-gradient(circle, #444 0%, #333 100%);
    background-size: cover;
    background-position: center;
    background-image: url("https://photo-arch-1306125602.cos.ap-shanghai.myqcloud.com/bgpic1.JPG");
}
.disk-cover::after {
    content: "";
    position: absolute;
    top: 50%;
    left: 50%;
    margin-left: -8px;
    margin-top: -8px;
    width: 16px;
    height: 16px;
    border-radius: 100%;
    background-image: linear-gradient(45deg, white, #dabad1);
    box-shadow: 0 1px 1px 1px rgba(0, 0, 0, 0.2);
}
.disk__playing {
    transform: translateY(-50%);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1),
        0 20px 20px -10px rgba(108, 29, 171, 0.3);
}
.disk__playing .disk-cover {
  animation: rotate infinite 6s linear;
}
@keyframes rotate {
  from {
    transform: rotate(0);
  }
  to {
    transform: rotate(360deg);
  }
}

.control {
    display: flex;
    height: 100%;

    align-items: center;
    justify-content: center;
}
.button {
    display: flex;
    margin: 2px;
    align-items: center;
    justify-content: center;
    // flex: 1;
    border-radius: 4px;
    color: #ccc;
    font-size: 16px;
    transition: background-color 0.6s ease;

    width: 35px;
    height: 35px;
}
@media (hover: hover) {
  .button:hover {
    background-color: #ddd;
    color: white;
  }
}
.button-side {
    font-size: 14px;
}

.progress {
    padding-left: 123px;
    padding-right: 12px;
    height: 100%;
    border-radius: 6px 6px 0 0;
    background-color: rgba(220, 220, 220, 0.5);
    transition: all 0.6s ease;
}
.progress__playing {
    transform: translateY(-100%);
}
.progress-title {
    padding-top: 6px;
    font-size: 12px;
    font-weight: bold;
    overflow: hidden;
    text-overflow: ellipsis;

    line-height: 15px;
}
.progress-text {
    padding-top: 2px;
    padding-left: 2px;
    font-size: 12px;
    font-weight: bold;
    color: #ccc;
    transform: scale(0.6);
    transform-origin: left top;

    margin-bottom: 0 !important;
    line-height: normal;
}
.bar {
    height: 3px;
    border-radius: 3px;
    overflow: hidden;
    background-color: #ddd;

    line-height: normal;
}
.bar span {
    display: block;
    height: 100%;
    background-color: #ec51a5;
}
</style>

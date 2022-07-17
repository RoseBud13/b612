<template>
    <div class="space">
        <!-- based on https://codepen.io/interaminense/full/QyGbXL/ -->
        <div class="noite"></div>
        <div class="constelacao"></div>
    </div>
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
    mounted() {
        this.initStars()
    },
    methods: {
        initStars() {
            //estrelas
            var style = ["style1", "style2", "style3", "style4", "style4", "style4"];
            var tam = ["tam1", "tam1", "tam1", "tam2", "tam3"];
            var opacity = ["opacity1", "opacity1", "opacity1", "opacity2", "opacity2", "opacity3"];

            function getRandomArbitrary(min, max) {
                return Math.floor(Math.random() * (max - min)) + min;
            }

            var estrela = "";
            var qtdeEstrelas = 43;
            var noite = document.querySelector(".constelacao");
            var widthWindow = 300;
            var heightWindow = 500;

            for (var i = 0; i < qtdeEstrelas; i++) {
                estrela += "<span class='estrela " + style[getRandomArbitrary(0, 6)] + " " + opacity[getRandomArbitrary(0, 6)] + " "
                + tam[getRandomArbitrary(0, 5)] + "' style='animation-delay: ." +getRandomArbitrary(0, 9)+ "s; left: "
                + getRandomArbitrary(0, widthWindow) + "px; top: " + getRandomArbitrary(0, heightWindow) + "px;'></span>";
            }

            noite.innerHTML = estrela;
        }
    }
})
</script>

<style scoped>
.space {
    background-color: rgba(0, 18, 51, 0.5);
    position: fixed;
    top: 0;
    left: 0;
    height: 100%;
    width: 100%;
    z-index: -1;
    text-align: center;
    overflow: hidden;
    border-radius: 15px;
}

.noite {
    background: -webkit-linear-gradient(top, rgb(0, 18, 51) 50%, rgb(25, 19, 39) 80%, rgb(0, 24, 69));
    width: 100%;
    height: 100%;
    position: absolute;
    overflow: hidden;
}

.constelacao {
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    animation: rotate 600s infinite linear;
    transform-origin: center center;
}

.estrela {
    background-color: white;
    border-radius: 50%;
    position: absolute;
    animation-name: estrela;
    animation-timing-function: linear;
    animation-iteration-count: infinite;
}

.estrela.style1 { animation-duration: 0.5s; animation-name: estrela; }
.estrela.style2 { animation-duration: 1s; animation-name: estrela; }
.estrela.style3 { animation-duration: 1.5s; animation-name: estrelaDestacada; }
.estrela.style4 { animation-duration: 2s; animation-name: estrelaDestacada; }

.estrela.tam1 { width: 1px; height: 1px; }
.estrela.tam2 { width: 2px; height: 2px; }
.estrela.tam3 { width: 3px; height: 3px; }

.estrela.opacity1 { opacity:  1; }
.estrela.opacity2 { opacity: .5; }
.estrela.opacity3 { opacity: .1; }


@keyframes escurecer {
    0%   { top: 0; }
    100% { top: 100%; }
}

@keyframes estrela {
    0% {
        box-shadow: 0 0 10px 0px rgba(255, 255, 255, 0.05);
    }
    50% {
        box-shadow: 0 0 10px 2px rgba(255, 255, 255, 0.4);
    }
    100% {
        box-shadow: 0 0 10px 0px rgba(255, 255, 255, 0.05);
    }
}

@keyframes estrelaDestacada {
    0% {
        background-color: #feeaba;
        box-shadow: 0 0 10px 0px rgba(255, 255, 255, 1);
    }
    20% {
        background-color: #FFC4C4;
        box-shadow: 0 0 10px 0px rgb(255, 196, 196, 1);
    }
    80% {
        background-color: #C4CFFF;
        box-shadow: 0 0 10px 0px rgb(196, 207, 255, 1);
    }
    100% {
        background-color: #ac71f0;
        box-shadow: 0 0 10px 0px rgba(185, 135, 193, 0.2);
    }
}

@keyframes rotate {
    0% {
        -webkit-transform: rotate(0deg);
    }
    100% {
        -webkit-transform: rotate(360deg);
    }
}
</style>

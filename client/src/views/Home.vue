<template>
    <div class="home">
        <space></space>
        <div id="mobile">
            <planet></planet>
            <continent-detail></continent-detail>
            <div class="arrow">
                <i class="fas fa-arrow-up"></i>
                <p>Drag Up</p>
            </div>
        </div>
    </div>
</template>

<script>
import Space from '../components/Space.vue'
import Planet from '../components/Planet.vue'
import ContinentDetail from '../components/ContinentDetail.vue'

export default {
    components: {
        Space,
        Planet,
        ContinentDetail
    }
}

</script>

<style lang="scss">
.home {
    width: 100vw;
    height: 100vh;
    position: relative;
    background: -webkit-linear-gradient(top, rgb(0, 18, 51) 50%, rgb(25, 19, 39) 80%, rgb(0, 24, 69));
}
#mobile {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    overflow: hidden;

    width: 25%;
    height: 90%;
    min-width: 375px;
    min-height: 667px;
    margin: 0 auto;

    border-radius: 13px;
    // box-shadow: 0 0 40px 0 rgba(0, 0, 0, 0.1);
    user-select: none;
    // transform: translate3d(0, 0, 0);
}
.arrow {
    position: absolute;
    bottom: 2%;
    left: 50%;
    transform: translateX(-50%);
    width: 50px;
    height: 50px;
    text-align: center;
    font-size: 20px;
    pointer-events: none;
    // animation: bounce-down 1.6s linear infinite;
}
.arrow p {
    font-size: 0.6em;
}

@media (max-width: 480px) {
    #mobile {
        width: auto;
        height: 100vh;
        min-width: auto;
        min-height: 100vh;
        border-radius: 0;
    }
}
@media (max-width: 480px) {
    .arrow {
        display: none;
    }
}
// @keyframes bounce-down {
//         25% {
//              transform: translateY(-4px);
//         }
//         50%, 100% {
//              transform: translateY(0);
//         }
//         75% {
//              transform: translateY(4px);
//         }
// }
</style>

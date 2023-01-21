<template>
    <div class="mini-slider">
        <div class="loop">
            <div class="wrap">
                <ul class="slider">
                    <li>
                        <img src="../../assets/img/flora1.jpg" alt="flower1">
                    </li>
                    <li>
                        <img src="../../assets/img/flora2.jpg" alt="flower1">
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>

</script>

<style lang="scss" scoped>
.mini-slider {
    width: 100%;
    height: 100%;
}

ul {
    list-style: none;
}

.loop {
    position: relative;
    width: 100%;
    height: 100%;
}

.wrap {
    position: relative;
    width: 100%;
    height: 100%;
    overflow: hidden;
    z-index: 2;
    border-radius: 30px;
}

.slider {
    width: 200%;
    height: 100%;
    text-align: center;
    color: #fff;
    margin-left: 0;
    animation: slide 12s ease-out infinite;
    -webkit-animation: slide 12s ease-out infinite;
}

.slider li {
    float: left;
    width: 50%;
    height: 100%;
}

.slider img {
    width: 100%;
    height: 100%;
}

/*创建三种动画策略*/
@keyframes slide {
    0% {
        margin-left: 0;
    }

    40% {
        margin-left: 0;
    }

    50% {
        margin-left: -100%;
    }

    90% {
        margin-left: -100%;
    }

    100% {
        margin-left: 0;
    }
}
@-webkit-keyframes slide {
    0% {
        margin-left: 0;
    }

    40% {
        margin-left: 0;
    }

    50% {
        margin-left: -100%;
    }

    90% {
        margin-left: -100%;
    }

    100% {
        margin-left: 0;
    }
}

@media (max-width: 600px) {
    .mini-slider {
        width: auto;
    }
}
</style>
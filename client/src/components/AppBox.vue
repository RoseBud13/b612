<template>
    <div class="app-box">
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
</template>

<script>

</script>

<style lang="scss" scoped>
.app-box {
    display: flex;
    flex-wrap: wrap;
    // align-content: flex-end;
    
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

@media (max-width: 1440px) {
    .icon-container {
        margin: 15px;
    }
}
</style>
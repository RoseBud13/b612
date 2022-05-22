<template>
    <div class="post-card">
        <input type="checkbox" name="" id="select">
        <label for="select" id="select-lable">
            <i class="fas fa-times"></i>
        </label>
        <div class="card">
            <div class="card-cover">
                <img src="../assets/img/planets.jpg" alt="img">
            </div>
            <div class="card-title">
                🪐&nbsp;B612星球的第一篇公开电报!&nbsp;🎉
            </div>
            <div class="content">
                <p>五月初开始，荒废了快一年的个人主页终于重新开始施工了。所谓的个人主页，也不仅仅是“我自己的”主页，希望以后这里可以有小伙伴们一同玩耍，每个人都能拥有一颗属于自己的星球&nbsp;🌍&nbsp;。</p>
                <p>困的不行了，我先睡一觉起来再好好写吧。</p>
                <p>💤</p>
                <br>
                <br>
                <br>
                <br>
                <br>
                <img src="../assets/img/cat_meme.jpg" alt="img">
            </div>
            <div class="card-footer">
                <div class="timestamp">
                    2022/5/23
                </div>
                <div class="card-icons">
                    <i class="fas fa-bookmark"></i>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

</script>

<style lang="scss" scoped>
#select {
    display: none;
}

.post-card {
    margin: 4px;
    position: relative;
}

.card {
    width: 100%;
    height: fit-content;
    background-color: #fff;
    border-radius: 10px;
    transition: all 0.6s;
}
.card::-webkit-scrollbar {
    display: none;
}

.card-cover {
    width: 100%;
    transition: all 0.6s;
}
.card-cover img {
    width: 100%;
    border-radius: 10px 10px 0 0;
    object-fit: cover;
    object-position: center;
}

.card-title {
    font-size: 1rem;
    color: rgba(88, 88, 88, 1);
    margin: 10px;
    transition: all 0.6s;
    transition-delay: 0.2s;
}

.content {
    display: none;
    height: fit-content;
    text-align: left;
    padding: 2rem 30% 10% 30%;
    font-size: 1.1rem;
    line-height: 1.7rem;
    background-color: #fff;
}
.content p {
    margin-bottom: 1.5rem;
}
.content img {
    margin: 2rem 0;
    width: 70%;
}

.card-footer {
    width: 100%;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
}

.timestamp {
    margin: 5px 10px 15px 10px;
    font-size: 0.8rem;
    color: rgb(75, 75, 75);
}

.card-icons i {
    margin: 5px 10px 15px 10px;
    font-size: 0.9rem;
    color: rgb(241, 78, 78);
}

#select-lable {
    display: block;
    position: absolute;
    top: 0;
    right: 0;
    width: 100%;
    height: 100%;
    z-index: 999;
    transition-delay: 0s;
}
#select-lable i {
    display: none;
    color: #fff;
}

#select:checked ~ .card {
    display: block;
    position: fixed;
    top: -50px;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: #fff;
    border-radius: 0;
    z-index: 999;

    overflow: auto;
}
#select:checked ~ #select-lable {
    position: fixed;
    top: 0;
    right: 1rem;
    width: 30px;
    height: 30px;
    background-color: rgb(200, 200, 200);
    border-radius: 50%;
    
    z-index: 9999;

    display: flex;
    justify-content: center;
    align-items: center;
    transition-delay: 0.6s;
}

#select:checked ~ #select-lable i {
    display: block;
}

#select:checked ~ .card .card-cover {
    height: 25vh;
    overflow: hidden;
}
#select:checked ~ .card .card-cover img {
    border-radius: 0;
}

#select:checked ~ .card .card-title {
    transform: translateY(-15vh);
    color: #fff;
    font-size: 2.5rem;
    text-align: center;
}

#select:checked ~ .card .card-footer {
    display: none;
}

#select:checked ~ .card .content {
    display: block;
    animation: content 2s;
    transform: translateY(-50px);
}

@keyframes content {
    from {
        opacity: 0;
        transform: translateY(0);
    }

    to {
        opacity: 1;
        transform: translateY(-50px);
    }
}

@media (max-width: 600px) {
    .content {
        padding: 0 10% 10% 10%;
        line-height: 30px;
        background-color: #fff;
    }
}
</style>
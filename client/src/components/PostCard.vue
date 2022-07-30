<template>
    <div class="post-card">
        <input type="checkbox" :id="post_select_id">
        <label :for="post_select_id">
            <i class="fas fa-times"></i>
        </label>
        <div class="card">
            <div class="card-cover">
                <img :src="post.post_cover" alt="img">
            </div>
            <div class="card-title">
                {{ post.post_title }}
            </div>
            <div class="content">
                <div v-html="post.post_content_text"></div>
                <img v-if="post.post_img_url.length" :src="post.post_img_url" alt="img">
            </div>
            <div class="card-footer">
                <div class="timestamp">
                    {{ post.post_timestamp }}
                </div>
                <div class="card-icons">
                    <p v-if="post.from=='ONE'">ONE·一个</p>
                    <i v-else-if="post.from=='admin'" class="fas fa-bookmark"></i>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { defineComponent } from "vue"

let PID = 1
export default defineComponent({
    props: {
        post: {
            type: Object,
            required: true
        }
    },
    data() {
        return {
            post_select_id: `post-${PID++}`,
        }
    }
})

</script>

<style lang="scss" scoped>
.post-card input {
    display: none;
}

.post-card {
    padding: 0 4px;
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
.content:deep(p) {
    margin-bottom: 1.5rem;
}
.content img {
    margin: 2rem 0;
    width: 60%;
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

.card-icons p {
    margin: 5px 10px 15px 10px;
    font-size: 0.7rem;
    color: rgb(222, 159, 159);
}

.post-card label {
    display: block;
    position: absolute;
    top: 0;
    right: 0;
    width: 100%;
    height: 100%;
    z-index: 99;
    transition-delay: 0s;
}
.post-card label i {
    display: none;
    color: #fff;
}

.post-card input:checked ~ .card {
    display: block;
    position: fixed;
    top: -50px;
    left: 0;
    width: 100vw;
    height: calc(100vh + 50px);
    background-color: #fff;
    border-radius: 0;
    z-index: 999;

    overflow: auto;
}
.post-card input:checked ~ label {
    position: fixed;
    top: 0.5rem;
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

.post-card input:checked ~ label i {
    display: block;
}

.post-card input:checked ~ .card .card-cover {
    height: 25vh;
    overflow: hidden;
}
.post-card input:checked ~ .card .card-cover img {
    border-radius: 0;
}

.post-card input:checked ~ .card .card-title {
    transform: translateY(-15vh);
    color: #fff;
    font-size: 2.5rem;
    text-align: center;
}

.post-card input:checked ~ .card .card-footer {
    display: none;
}

.post-card input:checked ~ .card .content {
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

    .content img {
        width: 100%;
    }
}
</style>
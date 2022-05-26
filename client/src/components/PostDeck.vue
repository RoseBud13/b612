<template>
    <div class="post-deck">
        <div class="masonry-view">
            <div class="masonry-item" v-for="post in posts" :key="post.post_id">
                <post-card :post="post"></post-card>
            </div>
        </div>
    </div>
</template>

<script>
import { defineComponent } from "vue"
import { getPostContent } from "../api"
import PostCard from './PostCard.vue'

export default defineComponent({
    components: {
        PostCard
    },
    data() {
        return {
            posts: []
        }
    },
    methods: {
        fetchPosts() {
            getPostContent().then(res => {
                this.posts = res.data
                // console.log(this.posts)
            }).catch(e => {
                console.log(e)
            })
        }
    },
    mounted() {
        this.fetchPosts()
    }
})

</script>

<style lang="scss" scoped>
.masonry-view {
    column-count: 5;
    column-gap: 0;
}
.masonry-item {
    padding-bottom: 8px;
}
.masonry-item img {
    display: block;
    width: 100%;
    height: auto;
    border-radius: 10px;
}

@media (max-width: 1300px) {
    .masonry-view {
        column-count: 4;
    }
}
@media (max-width: 1000px) {
    .masonry-view {
        column-count: 3;
    }
}
@media (max-width: 600px) {
    .masonry-view {
        column-count: 2;
    }
}
</style>
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
import { getOneSummary, getOneArticle, getPostContent } from "../api"
import PostCard from './PostCard.vue'

export default defineComponent({
    components: {
        PostCard
    },
    data() {
        return {
            dailyArticleInfo: {},
            posts: []
        }
    },
    methods: {
        fetchArticle() {
            getOneSummary().then(res => {
                this.dailyArticleInfo = {
                    'post_id': res.data.data.content_list[1].item_id,
                    'post_title': res.data.data.content_list[1].title.slice(0, -3),
                    'post_cover': 'https://b612.one/oneapi/img/' + res.data.data.content_list[1].img_url.slice(27),
                    'post_timestamp': res.data.data.content_list[1].post_date.slice(0, 10),
                    'post_img_url': 'https://b612.one/oneapi/img/' + res.data.data.content_list[1].img_url.slice(27)
                }
                return this.dailyArticleInfo.post_id
            }).then(data => {
                getOneArticle(data).then(res => {
                    // console.log(res.data)
                    const content_index_start = res.data.data.html_content.indexOf('</div></div></div><p>') + 18
                    const content_index_end = res.data.data.html_content.indexOf('</p>\n</div>\n') + 4
                    const content_str = res.data.data.html_content.slice(content_index_start, content_index_end)
                    // console.log(content_str)
                    this.dailyArticleInfo['post_content_text'] = content_str
                    this.posts.splice(2, 0, this.dailyArticleInfo)
                }).catch(e => {
                    console.log(e)
                })
            }).catch(e => {
                console.log(e)
            })
        },

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
        this.fetchPosts(),
        this.fetchArticle()
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
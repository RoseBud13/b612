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
            articleInfoList: [],
            posts: []
        }
    },
    methods: {
        fetchArticle() {
            getOneSummary().then(res => {
                res.data.data.content_list.forEach(item => {
                    if (item['content_type'] == '1') {
                        if (item['tag_list'].length == 0) {
                            this.articleInfoList.push({
                                'post_id': item.item_id,
                                'post_title': item.title.replace(/\s+/g, '').slice(0, -3),
                                'post_cover': 'https://b612.one/oneapi/img/' + item.img_url.slice(27),
                                'post_timestamp': item.post_date.slice(0, 10),
                                'post_img_url': 'https://b612.one/oneapi/img/' + item.img_url.slice(27),
                                'post_type': '文章',
                                'from': 'ONE'
                            })
                        } else {
                            this.articleInfoList.push({
                                'post_id': item.item_id,
                                'post_title': item.title,
                                'post_cover': 'https://b612.one/oneapi/img/' + item.img_url.slice(27),
                                'post_timestamp': item.post_date.slice(0, 10),
                                'post_img_url': 'https://b612.one/oneapi/img/' + item.img_url.slice(27),
                                'post_type': item['tag_list'][0]['title'].replace(/\s+/g, ''),
                                'from': 'ONE'
                            })
                        }
                    }
                })
                return this.articleInfoList
            }).then(data => {
                data.forEach((item, index) => {
                    index += 2
                    getOneArticle(item.post_id).then(res => {
                        if (item.post_type == '文章') {
                            const content_index_start = res.data.data.html_content.indexOf('</div></div></div><p>') + 18
                            const content_index_end = res.data.data.html_content.indexOf('</p>\n</div>\n') + 4
                            const content_str = res.data.data.html_content.slice(content_index_start, content_index_end)
                            item['post_content_text'] = content_str
                            this.posts.splice(index, 0, item)
                        } else if (item.post_type == '电台') {
                            const content_index_start = res.data.data.html_content.indexOf('</span></p><p>') + 11
                            const content_index_end = res.data.data.html_content.indexOf('</p><p></p>\n</div>\n') + 4
                            const content_str = res.data.data.html_content.slice(content_index_start, content_index_end)
                            item['post_content_text'] = content_str
                            this.posts.splice(index, 0, item)
                        } else if (item.post_type == '读诗') {
                            const content_index_start = res.data.data.html_content.indexOf('<p>&nbsp;</p><p style=\"text-align: center;\">') + 13
                            const content_index_end = res.data.data.html_content.indexOf('</p><p>&nbsp;</p><p class=') + 4
                            const content_str = res.data.data.html_content.slice(content_index_start, content_index_end)
                            item['post_content_text'] = content_str
                            this.posts.splice(index, 0, item)
                        } else if (item.post_type == '专栏') {
                            const content_index_start = res.data.data.html_content.indexOf('&nbsp;</div><p>') + 12
                            const content_index_end = res.data.data.html_content.indexOf('</p>\n</div>\n') + 4
                            const content_str = res.data.data.html_content.slice(content_index_start, content_index_end)
                            item['post_content_text'] = content_str
                            this.posts.splice(index, 0, item)
                        }
                    }).catch(e => {
                        console.log(e)
                    })
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
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
                        switch(item.post_type) {
                            case '文章':
                                const content1_index_start = res.data.data.html_content.indexOf('</div></div></div><p>') + 18
                                const content1_index_end = res.data.data.html_content.indexOf('</p>\n</div>\n') + 4
                                const content1_str = res.data.data.html_content.slice(content1_index_start, content1_index_end)
                                item['post_content_text'] = content1_str
                                this.posts.splice(index, 0, item)
                                break
                            case '电台':
                                const content2_index_start = res.data.data.html_content.indexOf('</span></p><p>') + 11
                                const content2_index_end = res.data.data.html_content.indexOf('</p><p></p>\n</div>\n') + 4
                                const content2_str = res.data.data.html_content.slice(content2_index_start, content2_index_end)
                                item['post_content_text'] = content2_str
                                this.posts.splice(index, 0, item)
                                break
                            case '读诗':
                                const content3_index_start = res.data.data.html_content.indexOf('<p>&nbsp;</p><p style=\"text-align: center;\">') + 13
                                const content3_index_end = res.data.data.html_content.indexOf('</p><p>&nbsp;</p><p class=') + 4
                                const content3_str = res.data.data.html_content.slice(content3_index_start, content3_index_end)
                                item['post_content_text'] = content3_str
                                this.posts.splice(index, 0, item)
                                break
                            case '专栏':
                                const content4_index_start = res.data.data.html_content.indexOf('&nbsp;</div><p>') + 12
                                const content4_index_end = res.data.data.html_content.indexOf('</p>\n</div>\n') + 4
                                const content4_str = res.data.data.html_content.slice(content4_index_start, content4_index_end)
                                item['post_content_text'] = content4_str
                                this.posts.splice(index, 0, item)
                                break
                            case '杂谈':
                                const content5_index_start = res.data.data.html_content.indexOf('box\">\n    <p>') + 10
                                const content5_index_end = res.data.data.html_content.indexOf('</p>\n</div>\n') + 4
                                const content5_str = res.data.data.html_content.slice(content5_index_start, content5_index_end)
                                item['post_content_text'] = content5_str
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
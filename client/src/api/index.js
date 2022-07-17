import request from '../utils/request'
import server from '../utils/server'

export function getOneQuote() {
    return request({
        method: 'get',
        url: 'oneapi/'
        // url: '/channel/one/0/0'
    })
}

export function getPostContent() {
    return request({
        method: 'get',
        url: 'static/post_content.json'
    })
}

export function verifyBpCode(data) {
    return server({
        method: 'post',
        url: 'api/verify-bp-code',
        data
    })
}

export function getPosts() {
    return server({
        method: 'get',
        url: 'api/posts'
    })
}
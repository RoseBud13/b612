import request from '../utils/request'

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
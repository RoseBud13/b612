import request from '../utils/request'
import server from '../utils/server'

export function getOneSummary() {
    return request({
        method: 'get',
        url: 'oneapi/'
        // url: '/channel/one/0/0'
    })
}

export function getOneArticle(essayId) {
    return request({
        method: 'get',
        url: `oneapi/essay/${essayId}`
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

export function userRegister(data) {
    return server({
        method: 'post',
        url: 'api/register-user',
        data
    })
}

export function userLogin(data) {
    return server({
        method: 'post',
        url: 'api/login',
        data
    })
}

export function getUser(uid) {
    return server({
        method: 'get',
        url: `api/user/${uid}`,
        // headers: {Authorization: token}
    })
}

export function updateUser(uid, data) {
    return server({
        method: 'put',
        url: `api/user/${uid}`,
        // headers: {Authorization: token},
        data
    })
}

export function getPosts() {
    return server({
        method: 'get',
        url: 'api/posts'
    })
}
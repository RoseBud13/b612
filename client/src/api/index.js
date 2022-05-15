import request from '../utils/request'

export function getOneQuote() {
    return request({
        method: 'get',
        url: 'oneapi/'
        // url: '/channel/one/0/0'
    })
}
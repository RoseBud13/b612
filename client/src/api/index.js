import oneApi from '../utils/request'

export function getOneQuote() {
    return oneApi({
        method: 'get',
        url: '/'
        // url: '/channel/one/0/0'
    })
}
const TokenKey = 'token';
const UserInfoKey = 'user-info';

export function getAuthToken() {
    return localStorage.getItem(TokenKey) ? localStorage.getItem(TokenKey) : null;
};

export function setAuthToken(token) {
    return localStorage.setItem(TokenKey, token);
};

export function removeAuthToken() {
    return localStorage.removeItem(TokenKey);
};

export function getAuthUserInfo() {
    let userInfoStr = localStorage.getItem(UserInfoKey);
    return userInfoStr ? JSON.parse(localStorage.getItem(UserInfoKey)) : null;
};

export function setAuthUserInfo(userInfo) {
    return localStorage.setItem(UserInfoKey, JSON.stringify(userInfo));
};

export function removeAuthUserInfo() {
    return localStorageStorage.removeItem(UserInfoKey);
};

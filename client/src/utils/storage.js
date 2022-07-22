const TokenKey = 'token';
const UserInfoKey = 'user-info';
const LocalSettingInfoKey = 'local-setting-info'

export const storage = {
    getAuthToken() {
        return localStorage.getItem(TokenKey) ? localStorage.getItem(TokenKey) : null;
    },
    setAuthToken(token) {
        return localStorage.setItem(TokenKey, token);
    },
    removeAuthToken() {
        return localStorage.removeItem(TokenKey);
    },
    getAuthUserInfo() {
        let userInfoStr = localStorage.getItem(UserInfoKey);
        return userInfoStr ? JSON.parse(localStorage.getItem(UserInfoKey)) : {'user-info': {'avatar': '', 'name': '', 'uid': '', 'username': ''}};
    },
    setAuthUserInfo(userInfo) {
        return localStorage.setItem(UserInfoKey, JSON.stringify(userInfo));
    },
    removeAuthUserInfo() {
        return localStorage.removeItem(UserInfoKey);
    },
    getLocalSettingInfo() {
        let localSettingInfoStr = localStorage.getItem(LocalSettingInfoKey);
        return localSettingInfoStr ? JSON.parse(localStorage.getItem(LocalSettingInfoKey)) : null;
    },
    setLocalSettingInfo(localSettingInfo) {
        return localStorage.setItem(LocalSettingInfoKey, JSON.stringify(localSettingInfo));
    },
    removeLocalSettingInfo() {
        return localStorage.removeItem(LocalSettingInfoKey);
    }
}

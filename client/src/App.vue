<template>
	<div id="app">
		<router-view></router-view>
	</div>
</template>

<script>
import { defineComponent, watch, getCurrentInstance, onMounted } from 'vue';
import { useStore } from 'vuex';
import router from './router';
import { storage } from './utils/storage'

export default defineComponent({
	setup() {
		const store = useStore();

		const { proxy } = getCurrentInstance();

		onMounted(() => {
			const userName = store.state.userInfo.name;
			const userUsername = store.state.userInfo.username;
            if (userName && userName.startsWith('unset_')) {
				// console.log(userName);
				// console.log(userUsername);
                router.push({name: 'user', params: { username: userUsername }});
				proxy.$toast('请完善昵称和邮箱', 'warning', 5000);
            }
        });

		watch(
			() => [store.state.userInfo.name, store.state.userInfo.username],
			(data) => {
				if (data[0] && data[0].startsWith('bday_')) {
					let localSetting = storage.getLocalSettingInfo();
					if (localSetting) {
						if (!localSetting.includes('bday_checked')) {
							localSetting.push('bday_checked');
							storage.setLocalSettingInfo(localSetting);
							window.location.href = "https://rosebud13.github.io/birthday/?name=%E5%AD%99%E5%A9%89%E5%AE%81&msg=%E6%88%91%E7%88%B1%E7%9A%84%E5%A5%B3%E5%AD%A9%EF%BC%8C%E7%94%9F%E6%97%A5%E5%BF%AB%E4%B9%90%E5%91%80";
						}
					} else {
						storage.setLocalSettingInfo(['bday_checked']);
						window.location.href = "https://rosebud13.github.io/birthday/?name=%E5%AD%99%E5%A9%89%E5%AE%81&msg=%E6%88%91%E7%88%B1%E7%9A%84%E5%A5%B3%E5%AD%A9%EF%BC%8C%E7%94%9F%E6%97%A5%E5%BF%AB%E4%B9%90%E5%91%80";
					}
				} else if (data[0] && data[0].startsWith('unset_')) {
					// console.log(data[0]);
					router.push({name: 'user', params: { username: data[1] }});
					proxy.$toast('请完善昵称和邮箱', 'warning', 5000);
				}
			}
		)
	}
})
</script>

<style>
/* @import url('https://cdn.bootcss.com/font-awesome/4.7.0/css/font-awesome.css'); */

* {
	margin: 0;
	padding: 0;
}

a {
	text-decoration: inherit;
}

ul,
ol {
	list-style: none;
}

h1,
h2,
h3,
h4 {
	font: inherit;
}

input,
select,
button {
	font: inherit;
}

html,
body {
	height: 100%;
	user-select: none;
	-webkit-touch-callout: none;
	-webkit-tap-highlight-color: transparent;
	overflow: hidden;
}

body {
	font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
		Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}

a:hover,
a:visited,
a:link,
a:active {
	text-decoration: none;
	color: inherit;
}

#app {
	height: 100%;
	overflow: hidden;
}
</style>

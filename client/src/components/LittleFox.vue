<template>
    <!-- based on https://codepen.io/AngelaVelasquez/pen/kMLJxG -->
    <div class="little-fox">
        <input type="checkbox" id="toggle" />
        <label for="toggle"></label>
        
        <div class="c-window">

            <span class="the-sun"></span>
            <span class="the-moon"></span>

            <div class="the-fox">
                <div class="fox-face">
                    <section class="eyes left"></section>
                    <section class="eyes right"></section>
                    <span class="nose"></span>
                    <div class="white-part"><span class="mouth"></span></div>
                </div>
            </div>

        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style lang="scss" scoped>
/* DAY STYLES*/

.little-fox {
    width: 100%;
    height: 100%;
}

.c-window {
    display: block;
    position: relative;
    width: 100%;
    height: 100%;
    margin-top: -100px;
    border-radius: 30px;
    background: #DDDDDD;
    overflow: hidden;
    transition: all .5s linear;
    -webkit-transition: all .5s linear;
}

.c-window .the-sun {
    display: block;
    position: relative;
    top: 18px;
    height: 40px;
    width: 40px;
    background: #FFE067;
    border-radius: 100%;
    margin: 0 auto;
    left: 30px;
}

.c-window .the-moon {
    position: relative;
    height: 24px;
    width: 24px;
    background: #EEE;
    border-radius: 100%;
    display: none;
}

.c-window .the-fox {
    display: block;
    position: absolute;
    bottom: -20px;
    height: 140px;
    width: 135px;
    margin: 0 50px;
    background: #E86A47;
    transition: bottom 1s;
    transition: bottom .15s ease-in-out;
    -webkit-transition: bottom .15s ease-in-out;
}

.c-window .the-fox:before {
    width: 0;
    height: 0;
    border-left: 0px solid transparent;
    border-right: 60px solid transparent;
    border-bottom: 30px solid #E86A47;
    top: -25px;
    left: 0;
    position: absolute;
    content: "";
}

.c-window .the-fox:after {
    width: 0;
    height: 0;
    border-right: 0px solid transparent;
    border-left: 60px solid transparent;
    border-bottom: 30px solid #E86A47;
    top: -30px;
    right: 0;
    position: absolute;
    content: "";
}

.c-window .the-fox:hover {
    bottom: -30px;
}

.c-window .the-fox .eyes {
    display: block;
    position: absolute;
    background: #FFFFFF;
    height: 15px;
    width: 15px;
    border-radius: 100%;
    bottom: 90px;
    transition: all .15s linear;
    -webkit-transition: all .15s linear;
}

.c-window .the-fox:hover .eyes {
    height: 2px;
    bottom: 97px;
}

.c-window .the-fox .eyes.left {
    left: 30px;
}

.c-window .the-fox .eyes.right {
    right: 30px;
}

.c-window .the-fox .nose {
    display: block;
    position: relative;
    background: #333;
    height: 12px;
    width: 12px;
    border-radius: 100%;
    margin: 0 auto;
    top: 50px;
}

.c-window .the-fox .white-part {
    display: block;
    position: relative;
    width: 0px;
    height: 0px;
    top: 55px;
    border-style: solid;
    border-width: 60px 70px 0 65px;
    border-color: #ffffff transparent transparent transparent;
}


input[type=checkbox] {
    position: absolute;
    visibility: hidden;
}

input#toggle[type=checkbox] {
    display: none;
}


label {
    position: relative;
    height: 100px;
    width: 100%;
    display: block;
    z-index: 9999;
    cursor: pointer;
    margin: 0;
}


/* NIGHT ANIMATION */

input[type=checkbox]:checked~.c-window {
    background: #222222;
}

input[type=checkbox]:checked~.c-window .the-sun {
    display: none;
}

input[type=checkbox]:checked~.c-window .the-moon {
    display: block;
    position: absolute;
    margin: 0 auto;
    top: 40px;
    left: 60px;
}

input[type=checkbox]:checked~.c-window .the-fox {
    background: #C74628;
}

input[type=checkbox]:checked~.c-window .the-fox:before {
    width: 0;
    height: 0;
    border-left: 0px solid transparent;
    border-right: 60px solid transparent;
    border-bottom: 30px solid #C74628;
    top: -30px;
    left: 0;
    position: absolute;
    content: "";
}

input[type=checkbox]:checked~.c-window .the-fox:after {
    width: 0;
    height: 0;
    border-right: 0px solid transparent;
    border-left: 60px solid transparent;
    border-bottom: 30px solid #C74628;
    top: -30px;
    right: 0;
    position: absolute;
    content: "";
}

input[type=checkbox]:checked~.c-window .the-fox .eyes {
    height: 2px;
    bottom: 90px;
}

input[type=checkbox]:checked~.c-window .the-fox:hover .eyes {
    height: 15px;
    bottom: 85px;
}

@media (max-width: 600px) {
    .little-fox {
        width: auto;
    }
    .c-window {
        width: 40vw;
        height: 40vw;
    }
}
</style>

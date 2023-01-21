<template>
    <div class="todo">
        <div class="todo-container">
            <p class="todo_tips">{{ taskAmount }} Tasks</p>
            <div class="todo_progress">
                <span class="todo_progress_line">
                    <i :style="{ width: progress, backgroundImage: progressColor }"></i>
                </span>
                <span class="todo_progress_num">{{ progress }}</span>
            </div>
            <div class="todo_tasks">
                <div class="add-task">
                    <input v-model="newTaskTitle" type="text" placeholder="Add new task">
                    <div class="task-sbmt" @click="addNewTask">
                        <i class="fas fa-plus"></i>
                    </div>
                </div>
                <h4 class="todo_subtitle" v-if="todayTasks.length">Today</h4>
                <ul>
                    <li v-for="task in todayTasks" :key="task.id">
                        <task :task="task" :showDate="false" />
                    </li>
                </ul>
                <h4 class="todo_subtitle" v-if="tomorrowTasks.length">Upcoming</h4>
                <ul>
                    <li v-for="task in tomorrowTasks" :key="task.id">
                        <task :task="task" :showDate="true" />
                    </li>
                </ul>
                <h4 class="todo_subtitle" v-if="outdatedTasks.length">Outdated</h4>
                <ul>
                    <li v-for="task in outdatedTasks" :key="task.id">
                        <task :task="task" :showDate="true" />
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
import { defineComponent } from 'vue'
import { mapMutations, mapState } from 'vuex'
import Task from './Task.vue'
import { today, tomorrow } from '../../utils/timechecker'

export default defineComponent({
    components: {
        Task
    },
    data() {
        return {
            colors: ['#ff6666', '#ffcccc'],
            newTaskTitle: ''
        }
    },
    methods: {
        ...mapMutations(['addTask']),
        addNewTask() {
            if (this.newTaskTitle) {
                let newTask = {
                    id: this.getRandomArbitrary(10, 100),
                    title: this.newTaskTitle,
                    date: new Date(),
                    done: false,
                    deleted: false
                }
                this.addTask(newTask)
                this.newTaskTitle = ''
            }
        },
        getRandomArbitrary(min, max) {
            return Math.random() * (max - min) + min
        }
    },
    computed: {
        ...mapState(['tasks']),
        taskAmount() {
            const totalCount = this.tasks.length
            let deletedCount = this.tasks.filter(t => t.deleted).length
            return totalCount - deletedCount
        },
        progress() {
            const totalCount = this.tasks.filter(t => !t.deleted).length
            const doneCount = this.tasks.filter(t => !t.deleted && t.done).length
            return `${Math.round((doneCount / totalCount) * 100)}%`
        },
        progressColor() {
            const colorLeft = `color-stop(30%, ${this.colors[0]})`
            const colorRight = `to(${this.colors[1]})`
            return `-webkit-gradient(linear, left bottom, right bottom, ${colorLeft}, ${colorRight})`
        },
        todayTasks() {
            return this.tasks.filter(task => {
                return task.date >= today && task.date < tomorrow && !task.deleted
            })
        },
        tomorrowTasks() {
            return this.tasks.filter(task => {
                return task.date >= tomorrow && !task.deleted
            })
        },
        outdatedTasks() {
            return this.tasks.filter(task => {
                return task.date < today && !task.deleted
            })
        }
    },
})
</script>

<style lang="scss" scoped>
.todo {
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}
.todo-container {
    width: 70%;
    max-width: 600px;
    height: 85%;
    max-height: 450px;
    padding: 20px;
    background-color: rgba(255, 255, 255, 0.7);
    border-radius: 20px;
}
.todo_tips {
    font-size: 1.1rem;
    font-weight: 600;
    margin: 20px 0 0 40px;
}
.todo_progress {
    display: flex;
    align-items: center;
    margin: 30px auto 20px auto;
    width: 70%;
}
.todo_progress_line {
    margin-right: 10px;
    flex: 1;
    height: 3px;
    background-color: #eee;

    i {
        display: block;
        height: 100%;
        transition: all 0.3s ease;
    }
}
.todo_progress_num {
    font-size: 0.7rem;
}
.todo_tasks {
    width: 70%;
    height: 75%;
    margin: 0 auto;
    overflow: auto;
}
.add-task {
    width: 100%;
    border-bottom: 1px solid #eee;
    padding: 5px 0;

    display: flex;
    justify-content: space-between;
}
.add-task input {
    width: 80%;
    line-height: 20px;
    border: 0;
    outline: none;
    background: none;
}
.add-task input:focus::placeholder {
  color: transparent;
}
.task-sbmt {
    line-height: 20px;
}
.task-sbmt i {
    padding: 0 10px;
    font-size: 16px;
    color: #808080;
    cursor: pointer;
}
.todo_tasks::-webkit-scrollbar {
    display: none;
}
.todo_subtitle {
    margin-top: 32px;
    margin-bottom: 8px;
    color: #808080;
}
@media (max-width: 820px) {
    .todo_tasks {
        height: 75%;
    }
}
@media (max-width: 600px) {
    .todo-container {
        width: 100%;
        max-width: 100%;
        height: 90%;
        max-height: 90%;
        padding: 20px;
    }
    .todo_progress {
        width: 95%;
    }
    .todo_tasks {
        width: 95%;
    }
}
</style>
<template>
    <div>
        <v-sheet class="pa-5" color="grey lighten-3">
            <v-card height="780">
                <v-card-title>
                    <v-row>
                    <span class="display-4 font-weight-black mx-4">{{Today.date}}</span>
                    <v-layout column justify-center wrap>
                        <span class="display-1 font-weight-bold">{{Month[Today.month]}}</span>
                        <span class="display-1 font-weight-bold">{{Today.year}}</span>
                    </v-layout>
                        <v-layout row class="justify-end align-center mr-8">
                                <!-- <v-btn class="ma-3 mr-6" color="info" outlined>未完了</v-btn> -->
                                <v-btn class="ma-3" color="info" fab outlined @click="showDialog('タスクの追加')">
                                    <v-icon>mdi-plus</v-icon>
                                </v-btn>
                        </v-layout>
                    </v-row>
                </v-card-title>

                <Editor ref="dialog"></Editor>
                <Viewer ref="view"></Viewer>

                <!-- <v-divider></v-divider> -->
                <v-tabs v-model="tab" grow>
                    <v-tab>未完了</v-tab>
                    <v-tab>完了済み</v-tab>
                    <!-- <v-tab>テーブル</v-tab> -->
                </v-tabs>
                <v-tabs-items v-model="tab">
                    <v-tab-item class="overflow-y-auto">
                        <v-container>
                            <v-col cols="12" v-if="msg.taskMessage != empty">
                                <v-alert type="info" outlined>{{ msg.taskMessage }}</v-alert>
                            </v-col>
                            <v-list two-line subheader max-height="580">
                            <v-list-item v-for="(task, index) in tasks" :key="index" @click="showViewer(index)">
                                <v-checkbox class="justify-center mr-2" color="teal" v-if="task.done == 1" input-value="true" @click.stop="checkTask(tasks[index].id, index)"></v-checkbox>
                                <v-checkbox exact class="justify-center mr-2" color="teal" v-if="task.done == 0" @click.stop="checkTask(tasks[index].id, index)"></v-checkbox>
                                <v-list-item-content>
                                        <v-list-item-title class="pl-3">{{ task.title }}</v-list-item-title>
                                        <v-row>
                                            <v-col cols="9">
                                                <v-list-item-subtitle class="pl-3" v-if="(task.due_t, task.due_t)!=empty && (task.due_t, task.due_t)!=null">期限 : {{ task.due_d }}&nbsp;&nbsp;{{ task.due_t}}</v-list-item-subtitle>
                                                <v-list-item-subtitle class="pl-3" v-else>&nbsp;</v-list-item-subtitle>
                                            </v-col>
                                            <v-col cols="3">
                                                <span v-if="task.priority==priCase.c0" class="body-2 ">&nbsp;</span>
                                                <span v-else-if="task.priority==priCase.c1" class="body-2 ">優先度 : 低</span>
                                                <span v-else-if="task.priority==priCase.c2" class="body-2 ">優先度 : 中</span>
                                                <span v-else-if="task.priority==priCase.c3" class="body-2 ">優先度 : 高</span>
                                            </v-col>
                                        </v-row>
                                    <v-divider></v-divider>
                                </v-list-item-content>
                                <v-list-item-action class="align-center justify-center action">
                                    <v-btn ref="btn" top icon @click.stop="showDialog('タスクの編集', index)">
                                        <v-icon>mdi-pencil</v-icon>
                                    </v-btn>
                                    <Editor ref="dialog" @updated="getTask()"></Editor>
                                </v-list-item-action>
                            </v-list-item>
                                </v-list>
                            </v-container>
                        </v-tab-item>

                    <!--完了済みタスクの画面-->
                    <v-tab-item class="overflow-y-auto">
                        <v-container>
                            <v-list two-line subheader max-height="580">
                            <v-col cols="12" v-if="msg.doneTaskMessage != empty">
                                <v-alert type="info" outlined>{{ msg.doneTaskMessage }}</v-alert>
                            </v-col>
                            <v-list-item v-for="(task, index) in done" :key="index" @click="showViewer(index, true)">
                                <v-checkbox class="justify-center mr-2" color="teal" v-if="task.done == 1" input-value="true" @click.stop="checkTask(task.id, index, true)"></v-checkbox>
                                <v-checkbox exact class="justify-center mr-2" color="teal" v-if="task.done == 0" @click.stop="checkTask(task.id, index, true)"></v-checkbox>
                                <v-list-item-content>
                                    <v-list-item-title class="pl-3">{{ task.title }}</v-list-item-title>
                                    <v-row>
                                        <v-col cols="9">
                                            <v-list-item-subtitle class="pl-3" v-if="(task.due_t, task.due_t)!=empty && (task.due_t, task.due_t)!=null">期限 : {{ task.due_d }}&nbsp;&nbsp;{{ task.due_t}}</v-list-item-subtitle>
                                            <v-list-item-subtitle class="pl-3" v-else>&nbsp;</v-list-item-subtitle>
                                        </v-col>
                                        <v-col cols="3">
                                            <span v-if="task.priority==priCase.c0" class="body-2 ">&nbsp;</span>
                                            <span v-else-if="task.priority==priCase.c1" class="body-2 ">優先度 : 低</span>
                                            <span v-else-if="task.priority==priCase.c2" class="body-2 ">優先度 : 中</span>
                                            <span v-else-if="task.priority==priCase.c3" class="body-2 ">優先度 : 高</span>
                                        </v-col>
                                    </v-row>
                                <v-divider></v-divider>
                            </v-list-item-content>
                            <v-list-item-action class="align-center justify-center action">
                                <v-btn ref="btn" top icon @click.stop="deleteTask(task.id)">
                                    <v-icon>mdi-trash-can</v-icon>
                                </v-btn>
                                <Editor ref="dialog" @updated="getTask()"></Editor>
                            </v-list-item-action>
                            </v-list-item>
                                </v-list>
                        </v-container>
                    </v-tab-item>
                </v-tabs-items>

                
            </v-card>
        </v-sheet>
    </div>
</template>

<script>
import Editor from "./TaskEditor"
import Viewer from "./TaskViewer"
import axios from 'axios'
var today = new Date()

export default {
    data () {
        return {
            msg : {
                taskMessage: '',
                doneTaskMessage: ''
            },
            tasks: '',
            done: '',
            selected: [],
            headers: [
                {
                    text: 'id',
                    align: 'left',
                    sortable: 'false',
                    value:'id'
                },
                {
                    text: 'title',
                    value: 'title'
                },
                {
                    text: 'due(date)',
                    value: 'due_d'
                },
                {
                    text: 'due(time)',
                    value: 'due_t'
                },
                {
                    text: 'priority',
                    value: 'priority'
                },
                { 
                    text: '操作',
                    align: 'center',
                    value: 'action',
                    sortable: false 
                }
            ],
            type : {
                edit : 'edit',
                add : 'add',
            },
            tab: null,
            empty: "",
            priCase : {
                "c0": 0,
                "c1": 1,
                "c2": 2,
                "c3": 3
            },
            Today: {
                "year": today.getFullYear(),
                "month": today.getMonth(),
                "date": today.getDate()
            },
            Month : ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
            }
    },
    components: {
        Editor,
        Viewer
    },
    methods: { 
        showDialog: function (type, set, done) {
            if(done == false || done == null){
                if(set==null){
                    console.log("Editor : Add mode")
                    this.$refs.dialog[0].open(type)
            }else{
                console.log("Editor : Edit mode, list from 'this.tasks'")
                var base = {
                    'id':this.tasks[set].id,
                    'title':this.tasks[set].title,
                    'due_d':this.tasks[set].due_d,
                    'due_t':this.tasks[set].due_t,
                    'priority':this.tasks[set].priority,
                    'description':this.tasks[set].description,
                    'done':this.tasks[set].done
                }
                console.log("base_task[ id : ", base.id, "] ====> edit")
                this.$refs.dialog[0].open(type, base)
            }  
            }else if(done == true){
                if(set==null){
                    console.log("Editor : Add mode(!)")
                    this.$refs.dialog[0].open(type)
                }else{
                    console.log("Editor : Edit mode, list from 'this.done'")
                    var base = {
                        'id':this.done[set].id,
                        'title':this.done[set].title,
                        'due_d':this.done[set].due_d,
                        'due_t':this.done[set].due_t,
                        'priority':this.done[set].priority,
                        'description':this.done[set].description,
                        'done':this.done[set].done
                    }
                    console.log("done_task[ id : ", base.id, "] ====> edit")
                    this.$refs.dialog[0].open(type, base)
                }
            }
        },
        showViewer: function (set, done) {
            if(done == false || done == null){
                if(set==null){
                    return
                }
                else{
                    // console.log("Viewer : list from 'this.tasks'")
                    var base = {
                        'id':this.tasks[set].id,
                        'title':this.tasks[set].title,
                        'due_d':this.tasks[set].due_d,
                        'due_t':this.tasks[set].due_t,
                        'priority':this.tasks[set].priority,
                        'description':this.tasks[set].description,
                        'done':this.tasks[set].done
                    }
                    // console.log(base)
                    console.log("base_task[ id : ", base.id, "] ====> to viewer")
                    this.$refs.view.open(base)
                }  
            }else if(done == true){
                if(set==null){
                    return
                }else{
                    // console.log("Viewer open, list from 'this.done'")
                    var base = {
                        'id':this.done[set].id,
                        'title':this.done[set].title,
                        'due_d':this.done[set].due_d,
                        'due_t':this.done[set].due_t,
                        'priority':this.done[set].priority,
                        'description':this.done[set].description,
                        'done':this.done[set].done
                    }
                    // console.log(this.$refs.view)
                    console.log("done_task[ id : ", base.id, "] ====> to Viewer")
                    this.$refs.view.open(base)
                }
            }
        },
        getTask: function(){
            const path = 'http://localhost:5000/api/tasks'
            var self = this
            this.msg.taskMessage = ""
            this.msg.doneTaskMessage = ""
            axios.get(path)
            .then(respons => {
                console.log(respons.data)
                if(respons.data==null){
                    this.data = {}
                }
                    if (respons.data.msg.msg_done == "None"){
                        this.msg.doneTaskMessage = "タスクはありません"
                    }
                    if (respons.data.msg.msg_task == "None"){
                        this.msg.taskMessage = "タスクはありません"
                    }
                    this.done = respons.data.done
                    this.tasks = respons.data.tasks
            })
            .catch(error => {
                console.log(error)
            })
        },
        checkTask (terget, index, done) {
            const path = 'http://localhost:5000/api/tasks/' + String(terget)
            // modify = this.tasks[index]
            if(done == false || done == null){
                var modify = {
                    'title': this.tasks[index].title,
                    'dueD': this.tasks[index].due_d,
                    'dueT': this.tasks[index].due_t,
                    'priority': this.tasks[index].priority,
                    'description' : this.tasks[index].description,
                    'done' : this.tasks[index].done
                }
            }else{
                var modify = {
                    'title': this.done[index].title,
                    'dueD': this.done[index].due_d,
                    'dueT': this.done[index].due_t,
                    'priority': this.done[index].priority,
                    'description' : this.done[index].description,
                    'done' : this.done[index].done
                }
            }
            if(modify.done == 0){
                modify.done = 1
            }
            else{
                modify.done = 0
            }
            // console.log(path, modify)
            if (typeof modify.description == "undefined"){
                    modify.description = ""
                }
            if (modify.priority == null || modify.done == null){
                console.error("Integer property is empty or null [input error, 'done' or 'priority']")
            }
            axios.put(path, modify)
            .then(response => {
                // console.log(response)
                this.getTask()
            })
            .catch(error => {
                console.log(error, this.id, modify)
                this.getTask()
            })
        },
        deleteTask: function(id){
            const path = 'http://localhost:5000/api/tasks/' + String(id)
            this.msg.taskMessage = ""
            this.msg.doneTaskMessage = ""
            axios.delete(path)
            .then(response => {
                    console.log("done_task[ id : ", id, "] ====> delete")
                    console.log(response)
                    this.getTask()
                })
                .catch(error => {
                    console.log(error, this.id)
                    this.getTask()
                })
        }
    },
    
    mounted:function () {
        const path = 'http://localhost:5000/api/tasks'
        var self = this
        axios.get(path)
        .then(respons => {
            if(respons.data==null){
                this.data = {}
            }
            // console.log(respons.data)
            if (respons.data.tasks == this.empty){
                this.tasks = [
                ]
                this.done = respons.data.done
                if (respons.data.msg.msg_done == "None"){
                    this.msg.doneTaskMessage = "タスクはありません"
                }
                if (respons.data.msg.msg_task == "None"){
                    this.msg.taskMessage = "タスクはありません"
                }
            }else{
                if (respons.data.msg.msg_done == "None"){
                    this.msg.doneTaskMessage = "タスクはありません"
                }
                if (respons.data.msg.msg_task == "None"){
                    this.msg.taskMessage = "タスクはありません"
                }
                this.done = respons.data.done
                this.tasks = respons.data.tasks
            }
        })
        .catch(error => {
            console.log(error)
        })
    },
}
</script>
<style>

</style>
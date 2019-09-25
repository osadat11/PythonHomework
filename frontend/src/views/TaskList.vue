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
                                <v-btn class="ma-3 mr-6" color="info" outlined>未完了</v-btn>
                                <v-btn class="ma-3" color="info" fab outlined @click="showDialog('タスクの追加')">
                                    <v-icon>mdi-plus</v-icon>
                                </v-btn>
                                <Editor ref="dialog"></Editor>
                        </v-layout>
                    </v-row>
                </v-card-title>

                <!-- <v-divider></v-divider> -->
                <v-tabs v-model="tab" grow>
                    <v-tab>未完了</v-tab>
                    <v-tab>完了済み</v-tab>
                    <v-tab>テーブル</v-tab>
                </v-tabs>
                <v-tabs-items v-model="tab">
                    <v-tab-item class="overflow-y-auto">
                        <v-container>
                            <v-list max-height="580">
                            <v-col cols="12" v-if="msg.taskMessage != empty">
                                <v-alert type="info" outlined>{{ msg.taskMessage }}</v-alert>
                            </v-col>
                            <v-list-item v-for="(task, index) in tasks" :key="index">
                                <v-col cols="1">
                                    <v-checkbox class="justify-center" color="teal" v-if="task.done == 1" input-value="true" @click.stop="checkTask(tasks[index].id)"></v-checkbox>
                                    <v-checkbox class="justify-center" color="teal" v-if="task.done == 0" @click.stop="checkTask(tasks[index].id)"></v-checkbox>
                                </v-col>
                                <v-list-item-content>
                                    <v-row>
                                        <v-col cols="12">
                                            <v-list-item-title class="pl-3">{{ task.title }}</v-list-item-title>
                                            <v-list-item-subtitle class="pl-3" v-if="(task.due_t, task.due_t)!=empty && (task.due_t, task.due_t)!=null">期限 : {{ task.due_d }}&nbsp;&nbsp;{{ task.due_t}}</v-list-item-subtitle>
                                            <v-list-item-subtitle class="pl-3" v-else>&nbsp;</v-list-item-subtitle>
                                        </v-col>
                                            <v-spacer></v-spacer>
                                    </v-row>
                                </v-list-item-content>
                                <v-row class="align-center justify-end">
                                    <v-col cols="3">
                                            <v-layout column justify-end>
                                                <span v-if="task.priority==priCase.c0" class="body-2">&nbsp;</span>
                                                <span v-else-if="task.priority==priCase.c1" class="body-2">優先度 : 低</span>
                                                <span v-else-if="task.priority==priCase.c2" class="body-2">優先度 ; 中</span>
                                                <span v-else-if="task.priority==priCase.c3" class="body-2">優先度 : 高</span>
                                            </v-layout>
                                    </v-col>
                                    <v-list-item-action>
                                        <v-btn icon @click="showDialog('タスクの編集', index)">
                                            <v-icon>mdi-pencil</v-icon>
                                        </v-btn>
                                        <Editor ref="dialog" @updated="getTask()"></Editor>
                                    </v-list-item-action>
                                </v-row>
                                </v-list-item>
                            </v-list>
                        </v-container>
                    </v-tab-item>

                    <v-tab-item>
                        <v-container>
                            <v-list max-height="580">
                                <v-col cols="12" v-if="msg.doneTaskMessage != empty">
                                    <v-alert type="info" outlined>完了済み{{ msg.doneTaskMessage }}</v-alert>
                                </v-col>
                            <v-list-item v-for="(task, index) in done" :key="index">
                                <v-col cols="1">
                                    <v-checkbox class="justify-center" color="teal" v-if="task.done == 1" input-value="true" @click="checkTask(task.id)"></v-checkbox>
                                    <v-checkbox class="justify-center" color="teal" v-if="task.done == 0" @click="checkTask(task.id)"></v-checkbox>
                                </v-col>
                                <v-list-item-content>
                                    <v-row>
                                        <v-col cols="12">
                                            <v-list-item-title class="pl-3">{{ task.title }}</v-list-item-title>
                                            <v-list-item-subtitle class="pl-3" v-if="(task.due_t, task.due_t)!=empty">期限 : {{ task.due_d }}&nbsp;&nbsp;{{ task.due_t}}</v-list-item-subtitle>
                                            <v-list-item-subtitle class="pl-3" v-else>&nbsp;</v-list-item-subtitle>
                                        </v-col>
                                            <v-spacer></v-spacer>
                                    </v-row>
                                </v-list-item-content>
                                <v-row class="align-center justify-end">
                                    <v-col cols="3">
                                            <v-layout column justify-end>
                                                <span v-if="task.priority==priCase.c0" class="body-2">&nbsp;</span>
                                                <span v-else-if="task.priority==priCase.c1" class="body-2">優先度 : 低</span>
                                                <span v-else-if="task.priority==priCase.c2" class="body-2">優先度 ; 中</span>
                                                <span v-else-if="task.priority==priCase.c3" class="body-2">優先度 : 高</span>
                                            </v-layout>
                                    </v-col>
                                    <v-list-item-action>
                                        <v-btn icon @click="showDialog('タスクの編集', index)">
                                            <v-icon>mdi-pencil</v-icon>
                                        </v-btn>
                                        <Editor ref="dialog" @updated="getTask()"></Editor>
                                    </v-list-item-action>
                                </v-row>
                                </v-list-item>
                            </v-list>
                        </v-container>

                    </v-tab-item>
                    <v-tab-item>
                        <v-data-table
                            v-model="selected"
                            :headers="headers"
                            :items="tasks"
                            show-select
                            single-select>
                            <template v-slot:item.action="{ item }">
                                <!-- <v-btn icon @click="showDialog('タスクの編集')">
                                    <v-icon>mdi-pencil</v-icon>
                                </v-btn>
                                <Editor ref="dialog" @updated="getTask()"></Editor> -->
                            </template>
                        </v-data-table>
                    </v-tab-item>
                </v-tabs-items>

                
            </v-card>
        </v-sheet>
    </div>
</template>

<script>
import Editor from "./TaskEditor"
import axios from 'axios'
var today = new Date()
console.log(today.getFullYear())
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
        Editor
    },
    methods: { 
        showDialog: function (type, set) {
            if(set==null){
                this.$refs.dialog[0].open(type)
            }else{
                var base = {
                    'id':this.tasks[set].id,
                    'title':this.tasks[set].title,
                    'due_d':this.tasks[set].due_d,
                    'due_t':this.tasks[set].due_t,
                    'priority':this.tasks[set].priority
                }
                console.log(base, " ====> edit")
                this.$refs.dialog[0].open(type, base)
            }
        },
        getTask: function(){
            const path = 'http://localhost:5000/api/tasks'
            var self = this
            axios.get(path)
            .then(respons => {
                if(respons.data==null){
                    this.data = {}
                }
                console.log(respons.data)
                if (respons.data.tasks == this.empty){
                    this.tasks = [
                        {
                        }
                    ]
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
                console.log(respons.data.tasks)
            })
            .catch(error => {
                console.log(error)
            })
        },checkTask (terget) {
            const path = 'http://localhost:5000/api/tasks/' + String(terget)
            var modify = {}
            modify = this.tasks[terget]
            if(modify.done == 0){
                modify.done = 1
            }else{
                modify.done = 0
            }
            console.log(path, modify)
            // axios.put(path, modify)
            // .then(response => {
            //     console.log(response)
            //     this.getTask()
            // })
            // .catch(error => {
            //     console.log(error, this.id, modify)
            //     this.getTask()
            // })
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
            console.log(respons.data)
            if (respons.data.tasks == this.empty){
                this.tasks = [
                    {
                    }
                ]
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
            console.log(respons.data.tasks)
        })
        .catch(error => {
            console.log(error)
        })
    },
}
</script>
<style>

</style>
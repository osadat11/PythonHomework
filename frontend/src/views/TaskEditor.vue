<template>
    <div>
        <v-row justify="center">
        <v-dialog v-model="dialog" persistent max-width="600px">
            <v-card>
            <v-card-title>
                <span class="display-1 font-weight-bold pa-3">{{ editor }}</span>
            </v-card-title>
            <v-card-text>
                <v-form v-model="valid" ref="form">
                <v-container>
                <v-row>
                    <v-col cols="12">
                    <v-text-field 
                        label="タイトル" 
                        v-model="title"
                        :counter="40" 
                        :rules="titleRules"
                        required
                        ></v-text-field>
                    </v-col>
                    <v-col cols="12">
                        <v-textarea
                            label="このタスクの説明"
                            v-model="description"
                            :counter="180"
                            :rules="descriptionRules"
                            maxlength="180"
                        ></v-textarea>
                    </v-col>

                    <v-col cols="6">
                        <v-menu
                            v-model="menu2"
                            :close-on-content-click="false"
                            :nudge-right="40"
                            transition="scale-transition"
                            offset-y
                            
                            min-width="290px"
                        >
                            <template v-slot:activator="{ on }">
                            <v-text-field
                                v-model="due_d"
                                label="期限(日付)"
                                v-on="on"
                                readonly
                                clearable
                            ></v-text-field>
                            </template>
                            <v-date-picker v-model="due_d" @input="menu2 = false"></v-date-picker>
                        </v-menu>
                    </v-col>

                    <v-col cols="6">
                    <v-menu
                        ref="menu"
                        v-model="tmenu"
                        :close-on-content-click="false"
                        :nudge-right="40"
                        :return-value.sync="due_t"
                        transition="scale-transition"
                        offset-y
                        
                        max-width="290px"
                        min-width="290px"
                    >
                        <template v-slot:activator="{ on }">
                        <v-text-field
                            v-model="due_t"
                            label="期限(時間)"
                            readonly
                            clearable
                            v-on="on"
                        ></v-text-field>
                        </template>
                        <v-time-picker
                        v-if="tmenu"
                        v-model="due_t"
                        format="24hr"
                        
                        scrollable
                        @click:minute="$refs.menu.save(due_t)"
                        ></v-time-picker>
                    </v-menu>
                    </v-col>

                    <v-subheader class="pl-2">優先度</v-subheader>
                    <v-col cols="12">
                    <v-slider
                        v-model="priority"
                        :tick-labels="priorities"
                        tick-size="4"
                        min="0"
                        max="3"
                        ticks="always"
                    >
                    </v-slider>
                    </v-col>
                </v-row>
                </v-container>
                </v-form>
                <v-divider></v-divider>
            </v-card-text>
            <v-card-actions>
                <div class="flex-grow-1"></div>
                <v-btn color="blue darken-1" text @click="reset(); close()">キャンセル</v-btn>
                <v-btn v-if="editor == types.add" color="blue darken-1" text @click="addTask()">追加</v-btn>
                <v-btn v-else-if="editor == types.edit" color="blue darken-1" text @click="updateTask()">保存</v-btn>
            </v-card-actions>
            </v-card>
        </v-dialog>
        </v-row>
    </div>
</template>
<script>
import axios from 'axios'
import { isString } from 'util'
export default {
    data: () => ({
        id: '',
        title: '',
        description: '',
        due_t:'',
        due_d: '',
        priority: 0,
        done:'',
        editor:'',
        types: {
                "edit" : "タスクの編集",
                "add" : "タスクの追加"
            },
        menu2: false,
        tmenu: false,
        valid: false,
        dialog : false,
        titleRules: [
            v => !!v || 'タイトルは必ず入力してください',
            v => (v && v.length <= 40) || 'タイトルは40文字以内で指定してください',
            v => {
                var nv = v
                if (typeof nv === "undefined"){
                    return false
                }else{
                    return !!(nv.replace(/\s+/g,""))||'空白のみの入力はできません';
                }
            },
            
        ],
        descriptionRules: [
            // v => (v.length > 0 && v.length <= 180) || '説明は180文字以内で指定してください',
            // v => !!(v && v.replace(/\s+/g, "")) || '空白のみの入力はできません'
        ],
        priorities: [
            'なし',
            '低',
            '中',
            '高'
        ],
        empty:""
    }),
    methods: {
        open(type, base) {
            if(base==null){
                this.editor = type
                this.dialog = true
            }else{
                this.editor = type
                this.dialog = true

                this.id = base.id
                this.title = base.title
                this.due_d = base.due_d
                this.due_t = base.due_t
                this.priority = base.priority
                this.description = base.description
                this.done = base.done
            }
        },
        close(){
            this.reset()
            this.dialog = false
        },
        validate () {
            if(this.$refs.form.validate()){
                this.snackbar = true
            }else{
                return true
            }
        },
        reset() {
            this.$refs.form.reset()
            this.due_t = ''
            this.due_d = ''
            this.description = ''
        },
        addTask () {
            if(!this.validate()){
                const path = 'http://localhost:5000/api/tasks'
                var task = {
                    'title': this.title,
                    'dueD': this.due_d,
                    'dueT': this.due_t,
                    'priority': this.priority,
                    'description' : this.description,
                    'done' : 0
                }
                if (task.priority == null || task.done == null){
                    console.error("Integer property is empty or null [input error, 'done' or 'priority']")
                }
                var msg = "タスク : " + this.title + "を作成しました"
                axios.post(path, task)
                .then(response => {
                    this.$emit('updated', msg, 1)
                })
                .catch(error => {
                    console.log(error)
                    this.$emit('updated', null, 1)
                })
                this.reset()
                this.close()
            }
        },
        updateTask () {
            if(!this.validate()){
                const path = 'http://localhost:5000/api/tasks/' + String(this.id)
                var modify = {
                    'title': this.title,
                    'dueD': this.due_d,
                    'dueT': this.due_t,
                    'priority': this.priority,
                    'description' : this.description,
                    'done' : this.done
                }
                if (typeof modify.description == "undefined"){
                    modify.description = ""
                }
                if (modify.priority == null || modify.done == null){
                    console.error("Integer property is empty or null [input error, 'done' or 'priority']")
                }
                var msg = "タスク : " + this.title + "を更新しました"
                axios.put(path, modify)
                .then(response => {
                    console.log(response)
                    this.$emit('updated', msg, 1)
                    this.close()
                })
                .catch(error => {
                    console.log(error, this.id, modify)
                    this.$emit('updated', null, 1)
                    this.close()
                })
            }
        },
    }
}
</script>
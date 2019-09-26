<template>
    <div>
        <v-row justify="center">
        <v-dialog v-model="dialog" persistent max-width="600px">
            <v-card>
            <v-card-title>
                タスクの詳細
            </v-card-title>
            <v-card-text>
                <v-container>
                <v-row>
                    <v-col cols="12">
                    <v-text-field 
                        label="タイトル" 
                        v-model="title" 
                        ></v-text-field>
                    </v-col>
                    <v-col cols="12">
                        <v-textarea
                            label="このタスクの説明"
                            v-model="description"
                            :counter="180"
                            editable=false
                        ></v-textarea>
                    </v-col>

                    <v-col cols="12">
                        <v-list-item-title class="pl-3">{{ task.title }}</v-list-item-title>
                        <v-list-item-subtitle class="pl-3" v-if="(task.due_t, task.due_t)!=empty && (task.due_t, task.due_t)!=null">期限 : {{ task.due_d }}&nbsp;&nbsp;{{ task.due_t}}</v-list-item-subtitle>
                        <v-list-item-subtitle class="pl-3" v-else>&nbsp;</v-list-item-subtitle>
                    </v-col>

                    <v-subheader class="pl-2">優先度</v-subheader>
                    <v-col cols="12">
                        {{ this.priority }}
                    </v-col>
                </v-row>
                </v-container>
                <v-divider></v-divider>
            </v-card-text>
            <v-card-actions>
                <div class="flex-grow-1"></div>
                <v-btn color="blue darken-1" text @click="close()">閉じる</v-btn>
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
        dialog : false,
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
        open(data) {
            this.editor = type
            this.dialog = true

            this.id = base.id
            this.title = base.title
            this.due_d = base.due_d
            this.due_t = base.due_t
            this.priority = base.priority
            this.description = base.description
            this.done = base.done
        },
        close(){
            this.reset()
            this.dialog = false
        }
    }
}
</script>
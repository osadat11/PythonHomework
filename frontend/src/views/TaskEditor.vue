<template>
    <div>
        <v-row justify="center">
        <v-dialog v-model="dialog" persistent max-width="600px">
            <v-card>
            <v-card-title>
                <span class="display-1 font-weight-bold pa-3">{{ editor }}</span>
            </v-card-title>
            <v-card-text>
                <v-form v-model="valid">
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
                            label="このタスクの詳細"
                            v-model="description"
                            counter="180"
                        ></v-textarea>
                    </v-col>

                    <v-col cols="6">
                        <v-menu
                            v-model="menu2"
                            :close-on-content-click="false"
                            :nudge-right="40"
                            transition="scale-transition"
                            offset-y
                            full-width
                            min-width="290px"
                        >
                            <template v-slot:activator="{ on }">
                            <v-text-field
                                v-model="date"
                                label="期限(日付)"
                                v-on="on"
                                readonly
                                clearable
                            ></v-text-field>
                            </template>
                            <v-date-picker v-model="date" @input="menu2 = false"></v-date-picker>
                        </v-menu>
                    </v-col>

                    <v-col cols="6">
                    <v-menu
                        ref="menu"
                        v-model="tmenu"
                        :close-on-content-click="false"
                        :nudge-right="40"
                        :return-value.sync="time"
                        transition="scale-transition"
                        offset-y
                        full-width
                        max-width="290px"
                        min-width="290px"
                    >
                        <template v-slot:activator="{ on }">
                        <v-text-field
                            v-model="time"
                            label="期限(時間)"
                            readonly
                            clearable
                            v-on="on"
                        ></v-text-field>
                        </template>
                        <v-time-picker
                        v-if="tmenu"
                        v-model="time"
                        format="24hr"
                        full-width
                        scrollable
                        @click:minute="$refs.menu.save(time)"
                        ></v-time-picker>
                    </v-menu>
                    </v-col>

                    <v-col cols="12">
                    <v-autocomplete
                        v-model="tag"
                        :items="['Skiing', 'Ice hockey', 'Soccer', 'Basketball', 'Hockey', 'Reading', 'Writing', 'Coding', 'Basejump']"
                        label="タグ"
                        multiple
                        chips
                        clearable
                    ></v-autocomplete>
                    </v-col>
                </v-row>
                </v-container>
                </v-form>
                <v-divider></v-divider>
            </v-card-text>
            <v-card-actions>
                <div class="flex-grow-1"></div>
                <v-btn color="blue darken-1" text @click="closeDialog">Close</v-btn>
                <v-btn v-if="editor == types[1]" color="blue darken-1" text @click="addTask(); closeDialog">Save</v-btn>
            </v-card-actions>
            </v-card>
        </v-dialog>
        </v-row>
    </div>
</template>
<script>
export default {
    name: 'Editor',
    props: {
        dialog: Boolean,
        editor: String
    },
    data: () => ({
        
        title: '',
        discription: '',
        time:'',
        tag:'',
        date: '',

        types: [
                'edit',
                'Add'
        ],

        menu2: false,
        tmenu: false,
        valid: false,
        dialog : false,
        titleRules: [
            v => !!v || 'タイトルは必ず入力してください',
            v => (v && v.length <= 40) || 'タイトルは40文字以内で指定してください',
        ]
    }),
    methods: {
        closeDialog(){
            this.$emit('closed');
        },
        addTask () {
            if (this.$refs.form.validate()) {
                this.snackbar = true
        }
            this.$valid.validateAll()
            const path = 'http://localhost:5000/tasks/add'
            var title = this.title
            var description = this.description
            let params = new URLSearchParams()
            params.append('title', title.value)
            params.append('description', description.value)
            console.log('newTitle : ' + title.value)
            console.log('newDesc : ' + description.value)
            title.value = ''
            description.value = ''
            // axios.post(path, params)
            //     .then(response => {
            //         var task = {'title': titleValue, 'description': descriptionValue}
            //         this.tasks.unshift(task)
            //         console.log(response)
            //     })
            //     .catch(error => {
            //         console.log(error)
            //     })
        }
    },
}
</script>
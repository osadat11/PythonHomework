<template>
    <div>
        <v-row justify="center">
        <v-dialog v-model="dialog" persistent max-width="600px">
            <template v-slot:activator="{ on }">
            <v-btn color="primary" dark v-on="on">Open Dialog</v-btn>
            </template>
            <v-card>
            <v-card-title>
                <span class="headline">タスクの編集</span>
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
                            v-model="discription"
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
                <v-btn color="blue darken-1" text @click="dialog = false">Close</v-btn>
                <v-btn color="blue darken-1" text @click="dialog = false">Save</v-btn>
            </v-card-actions>
            </v-card>
        </v-dialog>
        </v-row>
    </div>
</template>
<script>
export default {
    data: () => ({
        title: '',
        discription: '',
        date:'',
        time:'',
        tag:'',
        valid: false,
        dialog : false,
        date: new Date().toISOString().substr(0, 10),
        menu2: false,
        tmenu: false,
        titleRules: [
            v => !!v || 'タイトルは必ず入力してください',
            v => (v && v.length <= 40) || 'タイトルは40文字以内で指定してください',
        ]
    })
}
</script>
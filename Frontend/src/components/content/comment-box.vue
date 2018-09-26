<template>
    <div class="comment-box" :class="{notShowComment:!isShowComment,IsShowComment:isShowComment}">
      <el-container>
        <el-header>
          <span class="hotest">最热评论({{commentNum}})</span>
          <span class="go-comment-page">
            <span class="go-img"></span>
            <span>去评论页面</span>
          </span>
          <span class="close-button" @click="isShowComment=!isShowComment">
            <span class="close-img"></span>
          </span>
        </el-header>
        <el-main>
          <CommentLine :comments='comments' @sendReplyUser='getReplyUser'></CommentLine>
        </el-main>
        <el-footer>
          <div>
            <div class="enter-comment">
              <div class="reply-user">{{replyUser}}</div>
              <div class="enter-box-border">
                <textarea class="enter-box"></textarea>
              </div>
              <el-button>评论</el-button>
            </div>
            <div class="comment-button"></div>
          </div>
          <div>
            <div class="take-up-button">
              <span class="take-up-img"></span>
              <span @click="isShowComment=!isShowComment">收起</span>
            </div>
          </div>
        </el-footer>
      </el-container>
    </div>
</template>

<script>
import CommentLine from "./comment-line.vue";

export default {
  name: "CommentBox",
  props: ["comments", "commentNum"],
  data() {
    return {
      isShowComment: false,
      replyUser: ""
    };
  },
  methods: {
    showComment() {
      this.isShowComment = true;
    },
    getReplyUser(user) {
      this.replyUser = user;
    }
  },
  components: {
    CommentLine
  }
};
</script>

<style scoped>
.comment-box {
  margin-top: 10px;
  background: #eeeeee;
  font-size: 14px;
  border: solid 1px #e8d8d8;
  border-radius: 10px;
}

.comment-box .el-header {
  line-height: 60px;
  border-bottom: 1px dashed #887b7b;
}

.comment-box .el-main {
  border-bottom: 1px dashed #887b7b;
  padding: 10px 10px 20px 5px;
}

.comment-box .el-footer {
  height: 110px !important;
}

.hotest {
  font-weight: bold;
  opacity: 0.5;
}

.go-comment-page {
  margin-left: 20px;
  opacity: 0.6;
}
.go-comment-page:hover {
  text-decoration: underline;
  cursor: pointer;
}

.close-button:hover {
  cursor: pointer;
}

.go-img {
  background-image: url("./../../assets/pinglun.png");
  background-repeat: no-repeat;
  background-position: 0 -8px;
  height: 11px;
  width: 11px;
  display: inline-block;
}

.close-img {
  background-image: url("./../../assets/pinglun.png");
  background-repeat: no-repeat;
  background-position: 0 -38px;
  height: 11px;
  width: 11px;
  display: inline-block;
  margin-left: 75%;
}

.reply-user {
  margin-bottom: -10px;
  margin-left: 5px;
  margin-top: 5px;
  color: gray;
}

.enter-box-border {
  margin-top: 10px;
  padding: 5px;
  background: #e9f3ff;
  display: inline-block;
}

.enter-box {
  border: solid 1px #c4dcf7;
  height: 40px;
  font-size: 12px;
  width: 780px;
  min-height: 20px;
  padding: 4px 2px 0;
  line-height: 18px;
  overflow: auto;
  vertical-align: middle;
}

.take-up-button {
  margin-top: 7px;
  margin-left: 810px;
}

.take-up-img {
  background-image: url("./../../assets/pinglun.png");
  background-repeat: no-repeat;
  background-position: 0 -18px;
  height: 11px;
  width: 11px;
  display: inline-block;
}

.take-up-button {
  color: #a97e7e;
}
.take-up-button:hover {
  text-decoration: underline;
  cursor: pointer;
}

.notShowComment {
  display: none;
}

.IsShowComment {
  display: inline-block;
}
</style>



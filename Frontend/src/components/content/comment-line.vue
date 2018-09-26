<template>
    <div>
        <div class="comment-line indent" v-for="comment in comments" :key="comment.id">
            <div>
                <span @click="isExtend=!isExtend" :class="{HandImage:true,ExtendImg:isExtend,notExtendImg:!isExtend,NotHasChild:comment.child.length==0}">
                </span>
                <span>
                    <img class="user-img" :src="comment.userLogo">
                    <span class="user-name">{{comment.username}}</span>
                </span>
                <span class="user-comment">{{comment.commentText}}</span>
                <span>
                    <span class="user-time">{{comment.time}}</span>
                    <span class="user-device">{{comment.device}}</span>
                </span>
                <span class="user-opertions">
                    <span class="user-digg">顶[{{comment.diggNum}}]</span>
                    <span class="user-step-on">踩[{{comment.stepOnNum}}]</span>
                    <span class="user-report">举报</span>
                    <span class="user-reply-button" @click="reply(comment)">回复</span>
                </span>
            </div>
            <CommentLine :comments='comment.child' :class="{hide:!isExtend}" @sendReplyUser='getReplyUser'></CommentLine>
        </div>
    </div>
</template>

<script>
export default {
  name: "CommentLine",
  props: ["comments"],
  data() {
    return {
      isExtend: true
    };
  },
  methods: {
      reply(comment){
          this.$emit('sendReplyUser', `回复 ${comment.username}`)
      },
      getReplyUser(user){
          this.$emit('sendReplyUser', user)
      }
  }
};
</script>

<style scoped>
.indent {
  margin-top: 10px;
  margin-left: 15px;
}

.HandImage {
  background: url("./../../assets/pinglun_default.gif");
  background-repeat: no-repeat;
  height: 12px;
  width: 16px;
  display: inline-block;
  cursor: pointer;
}

.ExtendImg {
  background-position: -64px -45px;
}

.notExtendImg {
  background-position: -80px -13px;
}

.NotHasChild {
  background-position: 0 -1766px !important;
}

.comment-line {
  line-height: 17px;
  font-size: 12px;
  color: #b4b4b4;
  word-wrap: break-word;
  word-break: break-all;
}

.comment-line:hover {
  background: rgb(246, 236, 220);
}

.user-img {
  border: 1px solid #ccc;
  padding: 1px;
  width: 15px;
  height: 15jpx;
  vertical-align: bottom;
}

.user-name {
  color: #369;
}

.user-img,
.user-name:hover {
  cursor: pointer;
}

.user-comment {
  margin-left: 10px;
  color: black;
}

.user-time {
  margin-left: 10px;
}

.user-device {
  margin-left: 8px;
}

.user-opertions {
  margin-left: 20px;
  padding: 0 5px;
  border: 1px solid #e7d8bd;
  background: #fbf6ee;
  opacity: 0;
}

.user-opertions:hover {
  opacity: 1;
}

.user-opertions span {
  margin-left: 3px;
}

.user-opertions span:hover {
  color: #369;
  text-decoration: underline;
}

.hide {
  display: none;
}
</style>



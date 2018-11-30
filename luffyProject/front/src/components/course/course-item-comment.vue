<template>
  <div class="course-comment">
    <div class="comment-area">
      <div class="hot-evaluate-area">
        <span
          v-for="(hotComment, index) in hotCommentList"
          :key="index"
        >
          <img
            src="@/assets/teacher.png"
            style="display:block;height:65px;width:65px;"
          >
          <div>{{ hotComment.account }}</div>
          <div>{{ hotComment.content }}</div>
        </span>
      </div>
      <div class="all-evaluate-area">
        <div style="font-size: 18px;color: #333333; margin-top: 35px">全部评论</div>
        <div
          v-for="(comment, index) in commentList"
          :key="index"
          class="comment-item"
        >
          <img
            src="@/assets/teacher.png"
            style="display:inline-block;height:65px;width:65px;"
          >
          <div style="display:inline-block;margin-left: 21px; width: 727px">
            <div style="margin-top:5px;">{{comment.account}}</div>
            <div style="margin-top:5px;">{{comment.content}}</div>
            <div style="margin-top:5px;">{{comment.date}}</div>
          </div>
        </div>
      </div>
    </div>

    <div class="side">
      <div class="score">
        <div>
          <span style="font-size: 14px;color: #4A4A4A">综合评分</span>
          <span style="font-size: 14px;color: #4A4A4A; display: inline-block; margin-left: 30px;">15人评价</span>
        </div>
        <div style="font-size: 36px; margin: 4px 0; color: #FF9000">9.9</div>
        <ul style="margin-left:-65px;">
          <li>
            <div>通俗易懂</div>
            <div style="color: #FF9000">9.9分</div>
          </li>
          <li>
            <div>内容实用</div>
            <div style="color: #FF9000">9.9分</div>
          </li>
          <li>
            <div>讲解清晰</div>
            <div style="color: #FF9000">9.9分</div>
          </li>
        </ul>
      </div>
      <div class="labels">
        <div style="display: inline-block; margin: 30px 5px 15px 26px;font-size: 18px;color: #333333;letter-spacing: 0.29px">热门标签</div>
        <div>
          <el-col
            :span="9"
            :offset="2"
            v-for="(label, index) in labels"
            :key="index"
          ><span class="label">{{label}}</span></el-col>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "course-item-comment",
  data() {
    return {
      labels: ["讲解清晰", "内容实用", "通俗易懂", "老师很帅", "老司机"],
      commentList: [
        {
          account: "牛逼的人",
          content: "好牛逼啊",
          date: "两周前",
          sortNum: 1
        },
        {
          account: "牛逼的人",
          content:
            "听了几节感觉很不错，也比较好理解，再加上练习还是有进步的。希望这样的课程再多些就好了。",
          date: "两周前",
          sortNum: 2
        },
        {
          account: "牛逼的人",
          content: "好牛逼啊",
          date: "两周前",
          sortNum: 1
        },
        {
          account: "牛逼的人",
          content: "课程很好，期待后面更深入的教程",
          date: "两周前",
          sortNum: 2
        },
        {
          account: "牛逼的人",
          content: "好牛逼啊",
          date: "两周前",
          sortNum: 1
        },
        {
          account: "牛逼的人",
          content: "给老师点6666个赞 讲的太好了！！！课程不枯燥是最赞的",
          date: "两周前",
          sortNum: 2
        }
      ]
    };
  },
  computed: {
    hotCommentList() {
      return this.commentList.filter(item => item.sortNum == 2);
    }
  }
};
</script>

<style scoped>
.hot-evaluate-area {
  width: 100%;
  height: 310px;
  background: #fafafa;
  text-align: left;
}

.course-comment li {
  list-style-type: none;
  display: inline-block;
  margin: 30px;
  border-top: 1px solid #ff9000;
}

.comment-area {
  margin-left: 30px;
  display: inline-block;
  width: 980px;
}

.side {
  margin-left: 60px;
  display: inline-block;
  width: 325px;
  vertical-align: top;
}

.score {
  width: 100%;
  text-align: left;
  height: 200px;
  background: #fff5e6;
  padding: 34px 30px 34px 36px;
}

.side li div {
  font-size: 12px;
  color: #666666;
  display: block;
  margin-top: 11px;
}

.labels .label {
  width: 130px;
  height: 42px;
  background: #fafafa;
  border-radius: 2px;
  font-size: 14px;
  color: #9b9b9b;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  -ms-flex-pack: center;
  justify-content: center;
  margin-right: 26px;
  margin-bottom: 21px;
}

.hot-evaluate-area {
  width: 900px;
  margin: 0;
  padding: 0;
}

.hot-evaluate-area span {
  padding: 0 30px;
  width: 235px;
  height: 274px;
  text-align: center;
  border-right: 1px solid #d9dde0;
  display: inline-block;
  padding: 0 30px;
  text-align: center;
  border-right: 1px solid #d9dde0;
  vertical-align: top;
}

.comment-item {
  padding: 30px 0 22px;
  width: 100%;
  height: auto;
  background: #ffffff;
  box-shadow: 0 -1px 0 0 rgba(242, 242, 242, 0.5),
    0 1px 0 0 rgba(242, 242, 242, 0.5);
  border-bottom: solid #eee 1px;
}
</style>

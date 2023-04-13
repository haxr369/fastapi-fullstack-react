import axios from "axios";

const GetCommentList = async props => {

    /**
   * ^^^props^^^^
   * Compare_id
   * 비교 팁과 관련된 댓글들을 DB에서 가져오기.
   */
    const {Compare_id} = props;
    try {
        console.log("비교팁 ID : " + Compare_id);
        const rep = await axios.get(`/api/v1/comment/list/${Compare_id}`);
        //console.log(rep);
        return rep;
    } catch (ex) {
        console.log(ex);
        return -1;
    }

}

export default GetCommentList;
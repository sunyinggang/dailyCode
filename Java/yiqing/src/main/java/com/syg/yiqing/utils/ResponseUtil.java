package com.syg.yiqing.utils;

import com.syg.yiqing.entity.TraditionalOffice;
import org.springframework.data.domain.Page;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ResponseUtil {
    public static Object ok() {
        Map<String, Object> obj = new HashMap<String, Object>();
        obj.put("errno", 0);
        obj.put("errmsg", "成功");
        return obj;
    }

    public static Object ok(Object data) {
        Map<String, Object> obj = new HashMap<String, Object>();
        obj.put("errno", 0);
        obj.put("errmsg", "成功");
        obj.put("data", data);
        return obj;
    }

    public static Object okList(Page pagedata) {
        Map<String, Object> data = new HashMap<String, Object>();
        List list = pagedata.getContent();
        data.put("list", list);
        data.put("page", pagedata.getNumber()+1);
        data.put("totalPage", pagedata.getTotalPages());
        data.put("totalNum", pagedata.getTotalElements());
        return ok(data);
    }
}

package com.syg.yiqing.controller;

import com.syg.yiqing.entity.FutureRoom;
import com.syg.yiqing.entity.TraditionalOffice;
import com.syg.yiqing.service.FutureRoomService;
import com.syg.yiqing.utils.ResponseUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class FutureRoomController {

    @Autowired
    private FutureRoomService futureRoomService;

    @GetMapping("/room/list")
    public Object getList(@RequestParam(defaultValue = "1") Integer page,
                          @RequestParam(defaultValue = "上海") String city){
        PageRequest pageable = PageRequest.of(page-1,10);
        Page<FutureRoom> pageObject = futureRoomService.findAllByCity(pageable,city);

        return ResponseUtil.okList(pageObject);
    }

}

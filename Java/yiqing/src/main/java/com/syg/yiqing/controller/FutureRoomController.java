package com.syg.yiqing.controller;

import com.syg.yiqing.entity.FutureRoom;
import com.syg.yiqing.entity.TraditionalOffice;
import com.syg.yiqing.service.FutureRoomService;
import com.syg.yiqing.utils.ResponseUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.format.annotation.DateTimeFormat;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.time.LocalDateTime;
import java.util.Date;

@RestController
public class FutureRoomController {

    @Autowired
    private FutureRoomService futureRoomService;

    @GetMapping("/room/list")
    public Object getList(@RequestParam(defaultValue = "1") Integer page,
                          @RequestParam(required = false) String city,
                          @RequestParam(required = false) @DateTimeFormat(pattern = "yyyy-MM-dd") Date startTime,
                          @RequestParam(required = false) @DateTimeFormat(pattern = "yyyy-MM-dd") Date endTime){
        PageRequest pageable = PageRequest.of(page-1,10);
        //Page<FutureRoom> pageObject = futureRoomService.findAllByCity(pageable,city);
//        if(city == null){
//            city = "";
//        }
        Page<FutureRoom> pageObject2 = futureRoomService.findListLimitTime(pageable,city,startTime,endTime);
        return ResponseUtil.okList(pageObject2);
    }

}

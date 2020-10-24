package com.syg.yiqing.controller;

import com.syg.yiqing.entity.SignBuilding;
import com.syg.yiqing.entity.TraditionalOffice;
import com.syg.yiqing.service.SignBuildingService;
import com.syg.yiqing.service.TraditionalOfficeService;
import com.syg.yiqing.utils.ResponseUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.format.annotation.DateTimeFormat;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.time.LocalDateTime;
import java.util.List;

@RestController
public class TradicionalOfficeController {

    @Autowired
    private TraditionalOfficeService traditionalOfficeService;

    @GetMapping("/office/list")
    public Object getList(@RequestParam(defaultValue = "1") Integer page,
                          @RequestParam(required = false) String city,
                          @RequestParam(required = false) String openTime) {
        PageRequest pageable = PageRequest.of(page-1,10);
        Page<TraditionalOffice> pageObject = traditionalOfficeService.findListLimitTime(pageable,city,openTime);
        return ResponseUtil.okList(pageObject);
    }
}

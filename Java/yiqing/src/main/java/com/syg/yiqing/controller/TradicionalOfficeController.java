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
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class TradicionalOfficeController {

    @Autowired
    private TraditionalOfficeService traditionalOfficeService;

    @GetMapping("/office/list")
    public Object getList(@RequestParam(defaultValue = "1") Integer page,@RequestParam(defaultValue = "上海") String city) {
        PageRequest pageable = PageRequest.of(page-1,10);
        Page<TraditionalOffice> pageObject = traditionalOfficeService.findAll(pageable);
        Page<TraditionalOffice> pageObject2 = traditionalOfficeService.findAllByCity(pageable,city);
        return ResponseUtil.okList(pageObject2);
    }
}

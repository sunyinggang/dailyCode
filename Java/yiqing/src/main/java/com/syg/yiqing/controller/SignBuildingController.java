package com.syg.yiqing.controller;

import com.syg.yiqing.dao.SignBuildingDao;
import com.syg.yiqing.entity.SignBuilding;
import com.syg.yiqing.entity.TraditionalOffice;
import com.syg.yiqing.service.SignBuildingService;
import com.syg.yiqing.utils.ResponseUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class SignBuildingController {

    @Autowired
    private SignBuildingService signBuildingService;

    @GetMapping("/build/list")
    public Object getList(@RequestParam(defaultValue = "1") Integer page){
        PageRequest pageable = PageRequest.of(page-1,10);
        Page<SignBuilding> pageObject = signBuildingService.findAll(pageable);
        return ResponseUtil.okList(pageObject);
    }
}

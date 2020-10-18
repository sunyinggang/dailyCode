package com.syg.yiqing.controller;

import com.syg.yiqing.dao.BiddingGgzyDao;
import com.syg.yiqing.dao.PropertyDao;
import com.syg.yiqing.entity.BiddingGgzy;
import com.syg.yiqing.entity.Property;
import com.syg.yiqing.entity.SignBuilding;
import com.syg.yiqing.service.SignBuildingService;
import com.syg.yiqing.utils.ResponseUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class TempController {

    @Autowired
    private BiddingGgzyDao biddingGgzyDao;

    @GetMapping("/bidding/list")
    public Object getList(@RequestParam(defaultValue = "1") Integer page){
        PageRequest pageable = PageRequest.of(page-1,10);
        Page<BiddingGgzy> pageObject = biddingGgzyDao.findAll(pageable);
        return ResponseUtil.okList(pageObject);
    }

    @Autowired
    private PropertyDao propertyDao;

    @GetMapping("/property/list")
    public Object getPropertyList(@RequestParam(defaultValue = "1") Integer page){
        PageRequest pageable = PageRequest.of(page-1,10);
        Page<Property> pageObject = propertyDao.findAll(pageable);
        return ResponseUtil.okList(pageObject);
    }


}

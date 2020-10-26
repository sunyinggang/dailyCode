package com.syg.yiqing.controller;

import com.syg.yiqing.dao.*;
import com.syg.yiqing.entity.*;
import com.syg.yiqing.service.SignBuildingService;
import com.syg.yiqing.utils.ResponseUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

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

    @Autowired
    private OfficeBuildingDao officeBuildingDao;

    @GetMapping("/building/list")
    public Object getOfficeBuildingList(@RequestParam(defaultValue = "1") Integer page,
                                        @RequestParam(defaultValue = "上海") String city){
        PageRequest pageable = PageRequest.of(page-1,15);
        Page<OfficeBuilding> pageObject = officeBuildingDao.findAllByCity(pageable,city);
        return ResponseUtil.okList(pageObject);
    }

    @Autowired
    private WuyeAllDao wuyeAllDao;

    @GetMapping("/wuye/list")
    public Object getWuyeList(@RequestParam(defaultValue = "1") Integer page){
        PageRequest pageable = PageRequest.of(page-1,10);
        Page<WuyeAll> pageObject = wuyeAllDao.findAll(pageable);
        return ResponseUtil.okList(pageObject);
    }

    @Autowired
    private TraditionalOfficeDao traditionalOfficeDao;

    @Autowired
    private FutureRoomDao futureRoomDao;

    @Autowired
    private SignBuildingDao signBuildingDao;

    @GetMapping("/count/all")
    public Object getDataAll(){
        List<TraditionalOffice> objct1 =  traditionalOfficeDao.findAll();
        List<OfficeBuilding> objct2 =  officeBuildingDao.findAll();
        int office = objct1.size() + objct2.size();
        System.out.println(office);

        List<FutureRoom> objct3 =  futureRoomDao.findAll();
        System.out.println(objct3.size());

        List<BiddingGgzy> objct4 =  biddingGgzyDao.findAll();
        System.out.println(objct4.size());

        List<SignBuilding> objct5 =  signBuildingDao.findAll();
        System.out.println(objct5.size());

        return null;
    }

}

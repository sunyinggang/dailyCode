package com.syg.yiqing.service;

import com.syg.yiqing.dao.SignBuildingDao;
import com.syg.yiqing.entity.SignBuilding;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Service;

@Service
public class SignBuildingService {

    @Autowired
    private SignBuildingDao signBuildingDao;

    public Page<SignBuilding> findAll(PageRequest pageable){
        return signBuildingDao.findAll(pageable);
    }
}

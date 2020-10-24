package com.syg.yiqing.dao;

import com.syg.yiqing.entity.FutureRoom;
import com.syg.yiqing.entity.OfficeBuilding;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;

public interface OfficeBuildingDao extends JpaRepository<OfficeBuilding, Integer> {

    @Override
    Page<OfficeBuilding> findAll(Pageable pageable);

    Page<OfficeBuilding> findAllByCity(Pageable pageable,String city);
}
